# Generated by Django 4.2.2 on 2024-05-22 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0017_alter_preguntaseis_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preguntaseis',
            options={'verbose_name': 'Pregunta 6: Considerando que una Política de Descentralización de Chile contaría con una agenda de trabajo con un plazo de implementación a 10 años, ¿con cuál de las siguientes alternativas usted está más de acuerdo?'},
        ),
        migrations.AlterModelOptions(
            name='preguntasiete',
            options={'verbose_name': 'Pregunta 7: Para finalizar y considerando sus respuestas anteriores, ¿qué temática o medida agregaría, para serconsiderada en una Política de Descentralización de Chile? Esta pregunta es opcional.'},
        ),
    ]
