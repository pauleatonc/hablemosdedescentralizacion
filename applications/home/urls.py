from django.urls import path

from . import views

app_name = 'home_app'

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='index',
        ),
    path(
        'register-contact',
        views.ContactCreateView.as_view(),
        name = 'add-contact'
    ),
    path(
        'contact-success',
        views.ContactSuccess.as_view(),
        name = 'contact_success'
    ),
    
]