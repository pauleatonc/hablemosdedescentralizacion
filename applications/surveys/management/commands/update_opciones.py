from django.core.management.base import BaseCommand
from applications.surveys.models import OpcionesPreguntaCinco

class Command(BaseCommand):
    help = 'Actualiza los textos de OpcionesPreguntaCinco'

    def handle(self, *args, **kwargs):
        opciones = [
            ('1',
             '<strong>Institucionalizar una instancia de coordinación</strong> de los distintos niveles de gobierno (nacional, regional y comunal), a objeto de establecer de forma conjunta acciones estratégicas y de colaboración para el desarrollo de los territorios.'),
            ('2',
             '<strong>Exigir la presentación de programas</strong> de campaña para las candidaturas de alcalde o alcaldesa.'),
            ('3',
             '<strong>Impedir las candidaturas</strong> de gobernadores/as regionales y de alcaldes/as que se encuentren <strong>formalizados por casos de corrupción u otro tipo de delitos.</strong>'),
            ('4',
             '<strong>Orientar la distribución de competencias o atribuciones para cada nivel de gobierno (nacional, regional y local), distinguiendo las responsabilidades de cada uno.'),
            ('5',
             '<strong>Robustecer las finanzas de los gobiernos regionales y municipalidades,</strong> posibilitando nuevos ingresos con regulación de gastos.'),
            ('6',
             '<strong>Incorporar mayores mecanismos de control y rendición de cuentas</strong> de los recursos que administran los gobiernos regionales y municipalidades.'),
            ('7',
             '<strong>Fomentar la atracción y retención de técnicos y profesionales</strong> para que trabajen en comunas de menores recursos, mediante la difusión y/o creación de normas y programas públicos específicos.'),
        ]

        for clave, nuevo_texto in opciones:
            try:
                opcion = OpcionesPreguntaCinco.objects.get(clave=clave)
                opcion.texto = nuevo_texto
                opcion.save()
                self.stdout.write(self.style.SUCCESS(f'Opción {clave} actualizada correctamente.'))
            except OpcionesPreguntaCinco.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Opción {clave} no encontrada.'))
