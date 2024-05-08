from django.db import models
from django.contrib.auth.models import BaseUserManager

from django.db import models, IntegrityError
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, rut, password, is_staff, is_superuser, is_active, **extra_fields):
        # Inicialmente se asume que no hay errores.
        user = None
        error_message = ""

        try:
            user = self.model(
                rut=rut,
                is_staff=is_staff,
                is_superuser=is_superuser,
                is_active=is_active,
                **extra_fields
            )
            user.set_password(password)
            user.full_clean()  # Validar el modelo
            user.save(using=self.db)
        except IntegrityError:
            # Error generalmente causado por la violación de restricciones únicas, como RUT duplicado
            error_message = f"Ya existe un usuario con el RUT {rut}."
        except ValidationError as e:
            # Captura errores de validación del modelo
            error_message = ", ".join(e.messages)
        except Exception as e:
            # Captura cualquier otro error que pueda ocurrir.
            error_message = f"Error inesperado al crear el usuario: {str(e)}."

        # Si hay un mensaje de error, significa que algo salió mal.
        if error_message:
            raise ValueError(error_message)

        return user

    def create_user(self, rut, password=None, **extra_fields):
        return self._create_user(rut, password, False, False, True, **extra_fields)

    def create_superuser(self, rut, password=None, **extra_fields):
        return self._create_user(rut, password, True, True, True, **extra_fields)
