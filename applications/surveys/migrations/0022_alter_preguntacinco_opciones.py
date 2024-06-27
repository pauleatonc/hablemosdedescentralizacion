# Generated by Django 4.2.2 on 2024-05-31 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0021_alter_preguntacinco_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntacinco',
            name='opciones',
            field=models.CharField(choices=[('1', 'Institucionalizar una instancia de coordinación de los distintos niveles de gobierno (nacional, regional y comunal), a objeto de establecer de forma conjunta acciones estratégicas y de colaboración para el desarrollo de los territorios.'), ('2', 'Exigir la presentación de programas de campaña para las candidaturas de alcalde o alcaldesa.'), ('3', 'Impedir las candidaturas de gobernadores/as regionales y de alcaldes/as que se encuentren formalizados por casos de corrupción u otro tipo de delitos.'), ('4', 'Orientar la distribución de competencias o atribuciones para cada nivel de gobierno (nacional, regional y local), distinguiendo las responsabilidades de cada uno.'), ('5', 'Robustecer las finanzas de los gobiernos regionales y municipalidades, posibilitando nuevos ingresos con regulación de gastos.'), ('6', 'Incorporar mecanismos de control y rendición de cuentas de los recursos que administran los gobiernos regionales y municipalidades.'), ('7', 'Fomentar la atracción y retención de técnicos y profesionales para que trabajen en comunas de menores recursos, mediante la difusión y/o creación de normas y programas públicos específicos.'), ('8', 'No sabría responder')], max_length=2000, verbose_name='Selecciona tres opciones'),
        ),
    ]