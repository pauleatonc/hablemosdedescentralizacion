from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


from django.views.generic import (
    View,
)

from django.views.generic.edit import (
    FormView
)

from .forms import LoginForm

# Models
from .models import User


class LoginUser(FormView):
    template_name = 'apps/users/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(
            rut=form.cleaned_data['rut'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        # Agregamos un método para redirigir a la página desde donde se originó el login
        # en el html se debe agregar ?next={{ request.path }} a continuación del href {% url 'users_app:user-login' %}
        # para recoger el id del proyecto visitado
        next_url = self.request.GET.get('next', None)
        if next_url:
            return redirect(next_url)
        else:
            return redirect('home_app:index')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.request.META.get('HTTP_REFERER', '/'))