import environ
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
    'http://qahablemosdedescentralizacion.subdere.gob.cl',
    'http://www.qahablemosdedescentralizacion.subdere.gob.cl',
    '127.0.0.1'
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
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

# RECAPTCHA SETTINGS
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

# SENDGRID SETTINGS
SENDGRID_API_KEY = ''
ADMIN_EMAIL = ''
NOREPLY_EMAIL = ['noreply@bancoproyectos.subdere.gob.cl']

#Clave Única
CLAVE_UNICA_CLIENT_ID = ''
CLAVE_UNICA_CLIENT_SECRET =''
CLAVE_UNICA_REDIRECT_URI = ''

