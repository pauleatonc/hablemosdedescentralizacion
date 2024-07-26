from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from applications.home.admin import admin_site 

#urls errores 
from django.conf.urls import handler404 , handler500 
from applications.home.views import Error404 , Error500 , Error503


urlpatterns = [
    path('admin/', admin_site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.surveys.urls')),
    re_path('', include('applications.claveunica.urls')),
    re_path('', include('applications.noticiasymedia.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404.as_view()

handler500 = Error500.as_error_view()

urlpatterns += [
path('503/', Error503.as_error_view(), name='error_503'),
]
