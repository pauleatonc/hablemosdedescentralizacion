from django.urls import path
from .views import keycloak_login, keycloak_callback, keycloak_logout

app_name = 'claveunica'

urlpatterns = [
    path('keycloak_login/', keycloak_login, name='keycloak_login'),
    path('callback/', keycloak_callback, name='keycloak_callback'),
    path('keycloak_logout/', keycloak_logout, name='keycloak_logout'),
]