# views.py
import secrets
from django.shortcuts import redirect
from oauthlib.oauth2 import WebApplicationClient
from django.conf import settings
import urllib
import requests
from django.contrib.auth import login as auth_login  # Cambia el nombre de la importación para evitar conflictos
from django.contrib.auth import logout as auth_logout
from applications.users.models import User
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import get_user_model


#Paso 1
def generate_session_token():
    # Genera un token de sesión único de 32 caracteres de longitud
    return secrets.token_urlsafe(16)

#Paso 2
# Esta función maneja el inicio de la autenticación con Clave Única
def claveunica_login(request):
    # Creamos un cliente OAuth2 con el ID del cliente de Clave Única
    client = WebApplicationClient(settings.CLAVE_UNICA_CLIENT_ID)

    authorization_endpoint = 'https://accounts.claveunica.gob.cl/openid/authorize/'

    # Generar un token de sesión único
    token = generate_session_token()

    params = {
        'client_id': settings.CLAVE_UNICA_CLIENT_ID,
        'response_type': 'code',
        'scope': 'openid run name',
        'redirect_uri': settings.CLAVE_UNICA_REDIRECT_URI,
        'state': token,  # Agregamos el token de sesión único como parámetro
}

    # Construye la URL de solicitud de autorización con los parámetros
    uri = authorization_endpoint + '?' + urllib.parse.urlencode(params)

    request.session['oauth_state'] = token

    return redirect(uri)

# Esta función maneja el callback después de que el usuario se autentica con Clave Única
def callback(request):
    # Creamos un cliente OAuth2 con el ID del cliente de Clave Única
    client = WebApplicationClient(settings.CLAVE_UNICA_CLIENT_ID)

    # Obtener los parámetros de la redirección de ClaveÚnica
    authorization_response = settings.CLAVE_UNICA_REDIRECT_URI + '?' + request.META['QUERY_STRING']
    params = urllib.parse.parse_qs(urllib.parse.urlparse(authorization_response).query)

    # Obtener el valor de "state" de los parámetros de la redirección
    received_state = params.get('state', [None])[0]

    # Obtener el valor del token de sesión almacenado en la sesión del usuario
    stored_state = request.session.get('oauth_state')

    # Comparar los valores de "state" para confirmar que coinciden
    if received_state != stored_state:
        # Los valores de "state" no coinciden, lo que indica una solicitud sospechosa.
        # Realiza alguna acción de seguridad, como registrar el evento o rechazar la solicitud.
        # En este caso, redirige a una página de error o muestra un mensaje de error.

        # Por ejemplo, puedes redirigir a una página de error personalizada
        return HttpResponseBadRequest("Invalid state token")

    # Si los valores de "state" coinciden, procedemos a obtener el token de acceso y la información del usuario.

    # Preparamos la solicitud de token
    try:
        token_url, headers, body = client.prepare_token_request(
            'https://accounts.claveunica.gob.cl/openid/token/',
            authorization_response=authorization_response,
            redirect_url=settings.CLAVE_UNICA_REDIRECT_URI,
            client_secret=settings.CLAVE_UNICA_CLIENT_SECRET
        )
    except Exception as e:
        return JsonResponse({"error": f"Error preparing token request: {str(e)}"}, status=400)
    # Solicitamos el token
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(settings.CLAVE_UNICA_CLIENT_ID, settings.CLAVE_UNICA_CLIENT_SECRET),
    )
    # Verificar respuesta de solicitud de token
    if token_response.status_code != 200:
        return JsonResponse({"error": "Failed to retrieve access token from Clave Única."}, status=400)

    try:
    	# Parseamos la respuesta del token
        client.parse_request_body_response(token_response.text)
    except Exception as e:
        return JsonResponse({"error": f"Error parsing token response: {str(e)}"}, status=400)

    # Este es el endpoint de información del usuario de Clave Única
    userinfo_endpoint = 'https://accounts.claveunica.gob.cl/openid/userinfo/'

    # Preparamos la solicitud a la información del usuario
    try:
        uri, headers, body = client.add_token(userinfo_endpoint)
    except Exception as e:
        return JsonResponse({"error": f"Error preparing user info request: {str(e)}"}, status=400)

    # Solicitamos la información del usuario
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # Verificar respuesta de solicitud de información del usuario
    if userinfo_response.status_code != 200:
        return JsonResponse({"error": "Failed to retrieve user information from Clave Única."}, status=400)

    try:
    	# Parseamos la respuesta a la información del usuario
        userinfo = userinfo_response.json()
    except ValueError:
        return JsonResponse({"error": "Error parsing user information response."}, status=400)
    
    try:
        # Aquí obtenemos el rut del usuario a partir de la información de Clave Única
        rut = userinfo.get('RolUnico', {}).get('numero', '') + '-' + userinfo.get('RolUnico', {}).get('DV', '')
    except KeyError:
        return JsonResponse({"error": "Failed to retrieve RUT from user info."}, status=400)

    # Buscamos el usuario en nuestra base de datos o lo creamos si no existe
    User = get_user_model()
    try:
    	user, created = User.objects.get_or_create(
        	username=rut,  # Usamos el RUT como nombre de usuario
        	defaults={

            # Añade aquí cualquier otro campo de tu modelo de usuario que quieras llenar.
        }
    )
    except Exception as e:
        return JsonResponse({"error": f"Error creating or retrieving user from database: {str(e)}"}, status=500)

    if created:
        # Aquí puedes establecer cualquier valor por defecto o realizar cualquier otro procesamiento necesario para nuevos usuarios.
        pass

    # Autentica al usuario para la sesión actual.
    try:
        login(request, user)  # Usa el nombre de la función importada
    except Exception as e:
        return JsonResponse({"error": f"Error logging in user: {str(e)}"}, status=500)

    return redirect('/')

# Define la vista de logout
def logout(request):
    auth_logout(request)  # Cierra la sesión en tu aplicación Django

    # Construye la URL de logout de Clave Única
    logout_endpoint = 'https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout'
    post_logout_redirect_uri = 'https://www.hablemosdedescentralizacion.cl'  # URL a la que redirigir después del logout en tu aplicación
    logout_url = f"{logout_endpoint}?post_logout_redirect_uri={post_logout_redirect_uri}"

    return redirect(logout_url)  # Redirige al usuario al End-Session Endpoint de Clave Única

