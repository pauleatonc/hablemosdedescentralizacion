import environ
import os
from .base import *

# we load the variables from the .env file to the environment
env = environ.Env()
environ.Env.read_env()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-07n!hx-8et1p@wmnn0+w59x1g)qzxj^(m+)e&yrs#b6g7*m*-a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'qahablemosdedescentralizacion.subdere.gob.cl',
    'www.qahablemosdedescentralizacion.subdere.gob.cl',
    ]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    # Base de datos de aplicación
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hablemosdescentralizacion',
        'USER': 'postgres',
        'PASSWORD': 'Subdere.2022',
        'HOST': 'hablemos_db',
        'PORT': '5432',
        },
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")

# RECAPTCHA SETTINGS
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")

# SENDGRID SETTINGS
SENDGRID_API_KEY = env("SENDGRID_API_KEY")
ADMIN_EMAIL = env("ADMIN_EMAIL")
NOREPLY_EMAIL = env("NOREPLY_EMAIL")

#KEYCLOACK - Clave Única
LOGIN_URL = 'claveunica:keycloak_login'

KEYCLOAK_REALM = os.getenv('DEV_KEYCLOAK_REALM')
KEYCLOAK_AUTH_SERVER_URL = os.getenv('DEV_KEYCLOAK_AUTH_SERVER_URL')
KEYCLOAK_SSL_REQUIRED = os.getenv('DEV_KEYCLOAK_SSL_REQUIRED')
KEYCLOAK_RESOURCE = os.getenv('DEV_KEYCLOAK_RESOURCE')
KEYCLOAK_CREDENTIALS_SECRET = os.getenv('DEV_KEYCLOAK_CREDENTIALS_SECRET')
KEYCLOAK_CONFIDENTIAL_PORT = os.getenv('DEV_KEYCLOAK_CONFIDENTIAL_PORT')
KEYCLOAK_REDIRECT_URI = os.getenv('DEV_KEYCLOAK_REDIRECT_URI')
KEYCLOAK_TOKEN_URL = os.getenv('DEV_KEYCLOAK_TOKEN_URL')
KEYCLOAK_LOGOUT_URL = os.getenv('DEV_KEYCLOAK_LOGOUT_URL')
REDIRECT_URI_LOGOUT = os.getenv('DEV_KEYCLOAK_LOGOUT_URL')

