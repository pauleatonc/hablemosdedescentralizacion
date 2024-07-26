from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, login, logout as django_logout
from keycloak import KeycloakOpenID
from django.shortcuts import redirect
from django.conf import settings

from jose import jwt
import requests


def get_keycloak_config():
    return {
        'server_url': settings.KEYCLOAK_AUTH_SERVER_URL,
        'client_id': settings.KEYCLOAK_RESOURCE,
        'realm_name': settings.KEYCLOAK_REALM,
        'client_secret': settings.KEYCLOAK_CREDENTIALS_SECRET,
        'verify': True
    }


def create_keycloak_client(config):
    return KeycloakOpenID(
        server_url=config['server_url'],
        client_id=config['client_id'],
        realm_name=config['realm_name'],
        client_secret_key=config['client_secret'],
        verify=config['verify']
    )


def get_jwks_uri(server_url, realm_name):
    well_known_url = f"{server_url}/realms/{realm_name}/.well-known/openid-configuration"
    response = requests.get(well_known_url)
    if response.status_code == 200:
        oid_config = response.json()
        return oid_config.get('jwks_uri')
    else:
        raise Exception("Failed to load OIDC configuration")


def keycloak_login(request):
    config = get_keycloak_config()
    client = create_keycloak_client(config)
    auth_url = client.auth_url(redirect_uri=settings.KEYCLOAK_REDIRECT_URI, scope='openid claveUnica')
    return redirect(auth_url)


def keycloak_callback(request):
    config = get_keycloak_config()
    client = create_keycloak_client(config)
    code = request.GET.get('code')

    print("code: ", code)
    print("client: ", client)
    if not code:
        return JsonResponse({'error': 'No authorization code provided'}, status=400)

    try:
        redirect_uri = settings.KEYCLOAK_REDIRECT_URI
        token_response = client.token(grant_type='authorization_code', code=code, redirect_uri=redirect_uri)
        refresh_token = token_response.get('refresh_token')
        print("Refresh token 1: ", refresh_token)
        request.session['refresh_token'] = refresh_token
        access_token = token_response['access_token']
        jwks_uri = get_jwks_uri(config['server_url'], config['realm_name'])
        jwks = requests.get(jwks_uri).json()

        header = jwt.get_unverified_header(access_token)
        kid = header['kid']
        rsa_key = next((key for key in jwks["keys"] if key["kid"] == kid), None)
        if rsa_key:
            try:
                # Decoding the token using the RSA key
                payload = jwt.decode(
                    access_token,
                    rsa_key,
                    algorithms=['RS256'],
                    audience='your-audience'
                )
                print("Decoded JWT payload:", payload)
            except jwt.JWTError as e:
                print("JWT Error:", e)

            # Extraer información del payload
            rut_numero = payload.get("rut_numero")
            rut_dv = payload.get("rut_dv")
            rut = f"{rut_numero}-{rut_dv}"

            # Verificar si el usuario existe y loguear o crear
            User = get_user_model()
            user, created = User.objects.get_or_create(rut=rut)
            if created:
                print("Nuevo usuario creado:", rut)
            else:
                print("Usuario existente, se ha logueado:", rut)

            # Loguear al usuario automáticamente
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect('/onboarding')
    except Exception as e:
        print("Error details:", e)
        return JsonResponse({'error': str(e)}, status=500)


def keycloak_logout(request):
    print("entra al método logout")
    keycloak_config = get_keycloak_config()

    # Aquí asumimos que obtienes el refresh_token de alguna manera segura
    # Podría ser desde la sesión, una cookie segura, o directamente del cuerpo de la solicitud
    refresh_token = request.session.pop('refresh_token', None)

    print("Solicita refresh token: ", refresh_token)

    client_id = keycloak_config['client_id']
    client_secret = keycloak_config['client_secret']
    logout_url = keycloak_config['server_url'] + '/realms/' + keycloak_config[
        'realm_name'] + '/protocol/openid-connect/logout'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
    }

    # Hacer la solicitud de cierre de sesión a Keycloak
    response = requests.post(logout_url, headers=headers, data=payload)
    print("response", response)

    if response.status_code in [200, 204]:  # Verifica si la respuesta es exitosa
        django_logout(request)  # Cierra la sesión en Django
        return redirect('home_app:index')
    else:
        return redirect('home_app:index')
