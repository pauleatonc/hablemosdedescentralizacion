import environ
from .base import *
import os

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
    'http://qahablemosdedescentralizacion.subdere.gob.cl',
    'http://www.qahablemosdedescentralizacion.subdere.gob.cl',
    'http://127.0.0.1:8000/',
    '127.0.0.1',
    'http://localhost:8000/',
    'localhost'
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
        'HOST': 'localhost',
        'PORT': '5432',
        },
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'modernizacion@subdere.gov.cl'
EMAIL_HOST_PASSWORD = 'Subde*moder23'
EMAIL_PORT = 587

# RECAPTCHA SETTINGS
RECAPTCHA_PUBLIC_KEY = '6LemsJgmAAAAAJj8noe-1FWZgl0ltkX5SeGgBa0h'
RECAPTCHA_PRIVATE_KEY = '6LemsJgmAAAAAG8rwzcmMJVPx1t8VLpT86vWju-i'

# SENDGRID SETTINGS
SENDGRID_API_KEY = ''
ADMIN_EMAIL = ''
NOREPLY_EMAIL = ['noreply@bancoproyectos.subdere.gob.cl']

#Clave Única
CLAVE_UNICA_CLIENT_ID = 'f0a29848899147da8e17f90d7b8a142e'
CLAVE_UNICA_CLIENT_SECRET ='55bdcfe678324f7baf7f559dd5c35aeb'
CLAVE_UNICA_REDIRECT_URI = 'https://www.qadescentralizacion.subdere.gob.cl/pregunta-uno/'

# LOCAL KEYCLOAK CONFIGURATION
KEYCLOAK_REALM='app-qa'
KEYCLOAK_AUTH_SERVER_URL='https://oid.subdere.gob.cl/'
KEYCLOAK_SSL_REQUIRED='external'
KEYCLOAK_RESOURCE='hablemosdescentralizacion'
KEYCLOAK_CREDENTIALS_SECRET='aSiHvZa5YwtGQRUDsEFJN5imFGcYqsa6'
KEYCLOAK_CONFIDENTIAL_PORT=0
KEYCLOAK_REDIRECT_URI='http://localhost:8000'
KEYCLOAK_TOKEN_URL='https://oid.subdere.gob.cl/realms/app-qa/protocol/openid-connect/token'
KEYCLOAK_LOGOUT_URL='https://oid.subdere.gob.cl/realms/app-qa/protocol/openid-connect/logout'
KEYCLOAK_LOGOUT_URL='http://localhost:8000'