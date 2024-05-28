import environ
import os
from .base import *

# we load the variables from the .env file to the environment
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    # Base de datos de aplicación
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILES_LOCATION = 'media'

# Bucket Storage Configuration
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")  # e.g. us-west-2
AWS_S3_FILE_OVERWRITE = env.bool('AWS_S3_FILE_OVERWRITE', default=False)
AWS_DEFAULT_ACL = None

# EMAIL SETTINGS
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
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

# Clave Única
CLAVE_UNICA_CLIENT_ID = env("CLAVE_UNICA_CLIENT_ID")
CLAVE_UNICA_CLIENT_SECRET = env("CLAVE_UNICA_CLIENT_SECRET")
CLAVE_UNICA_REDIRECT_URI = env("CLAVE_UNICA_REDIRECT_URI")

# KEYCLOACK - Clave Única
LOGIN_URL = 'claveunica:keycloak_login'

KEYCLOAK_REALM = os.getenv('KEYCLOAK_REALM')
KEYCLOAK_AUTH_SERVER_URL = os.getenv('KEYCLOAK_AUTH_SERVER_URL')
KEYCLOAK_SSL_REQUIRED = os.getenv('KEYCLOAK_SSL_REQUIRED')
KEYCLOAK_RESOURCE = os.getenv('KEYCLOAK_RESOURCE')
KEYCLOAK_CREDENTIALS_SECRET = os.getenv('KEYCLOAK_CREDENTIALS_SECRET')
KEYCLOAK_CONFIDENTIAL_PORT = os.getenv('KEYCLOAK_CONFIDENTIAL_PORT')
KEYCLOAK_REDIRECT_URI = os.getenv('KEYCLOAK_REDIRECT_URI')
KEYCLOAK_TOKEN_URL = os.getenv('KEYCLOAK_TOKEN_URL')
KEYCLOAK_LOGOUT_URL = os.getenv('KEYCLOAK_LOGOUT_URL')
REDIRECT_URI_LOGOUT = os.getenv('KEYCLOAK_LOGOUT_URL')

# Trusted origins for the CSRF validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# If we are behind proxy with https we trust the header defined here.
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = env.tuple('SECURE_PROXY_SSL_HEADER', default=None)
