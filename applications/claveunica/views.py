# views.py
from django.shortcuts import redirect
from oauthlib.oauth2 import WebApplicationClient
from django.conf import settings
import urllib
import requests 
from django.contrib.auth import login as auth_login  # Cambia el nombre de la importación para evitar conflictos
from users.models import User

# Esta función maneja el inicio de la autenticación con Clave Única
def claveunica_login(request):  
    client = WebApplicationClient(settings.CLAVE_UNICA_CLIENT_ID)

    # Este es el endpoint de autorización de Clave Única
    authorization_endpoint = 'https://accounts.claveunica.gob.cl/openid/authorize/'

    # Preparamos la URL de redirección al endpoint de autorización
    uri, state = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=settings.CLAVE_UNICA_REDIRECT_URI,
        scope=["openid", "email", "profile"],
    )

    # Guardamos el estado en la sesión para poder comprobarlo más tarde
    request.session['oauth_state'] = state

    # Redirigimos al usuario a la página de autorización de Clave Única
    return redirect(uri)

# Esta función maneja el callback después de que el usuario se autentica con Clave Única
def callback(request):
    # Creamos un cliente OAuth2 con el ID del cliente de Clave Única
    client = WebApplicationClient(settings.CLAVE_UNICA_CLIENT_ID)

    # Este es el endpoint de token de Clave Única
    token_endpoint = 'https://accounts.claveunica.gob.cl/openid/token/'
    authorization_response = settings.CLAVE_UNICA_REDIRECT_URI + '?' + request.META['QUERY_STRING']

    # Preparamos la solicitud de token
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=authorization_response,
        redirect_url=settings.CLAVE_UNICA_REDIRECT_URI,
        client_secret=settings.CLAVE_UNICA_CLIENT_SECRET
    )

    # Solicitamos el token
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(settings.CLAVE_UNICA_CLIENT_ID, settings.CLAVE_UNICA_CLIENT_SECRET),
    )

    # Parseamos la respuesta del token
    client.parse_request_body_response(token_response.text)

    # Este es el endpoint de información del usuario de Clave Única
    userinfo_endpoint = 'https://accounts.claveunica.gob.cl/openid/userinfo/'

    # Preparamos la solicitud a la información del usuario
    uri, headers, body = client.add_token(userinfo_endpoint)

    # Solicitamos la información del usuario
    userinfo_response = requests.get(uri, headers=headers, data=body)

     # Parseamos la respuesta a la información del usuario
    userinfo = userinfo_response.json()

    # Aquí obtenemos el rut del usuario a partir de la información de Clave Única
    rol_unico = userinfo.get('RolUnico')
    rut = f"{rol_unico['numero']}-{rol_unico['DV']}"

    # Buscamos el usuario en nuestra base de datos o lo creamos si no existe
    user, created = User.objects.get_or_create(
        username=userinfo['sub'],
        defaults={
            'rut': rut,
            # Añade aquí cualquier otro campo de tu modelo de usuario que quieras llenar.
        }
    )

    if created:
        # Aquí puedes establecer cualquier valor por defecto o realizar cualquier otro procesamiento necesario para nuevos usuarios.
        pass

    # Autentica al usuario para la sesión actual.
    auth_login(request, user)  # Usa el nombre de la función importada

    return redirect('/')