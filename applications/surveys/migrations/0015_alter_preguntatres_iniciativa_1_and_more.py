# Generated by Django 4.2.2 on 2024-05-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0014_alter_preguntatres_iniciativa_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntatres',
            name='iniciativa_1',
            field=models.IntegerField(choices=[(1, 'Gobierno Regional'), (2, 'Municipalidad'), (3, 'No sabría responder')], help_text='Ambientales', verbose_name='Ambientales'),
        ),
        migrations.AlterField(
            model_name='preguntatres',
            name='iniciativa_2',
            field=models.IntegerField(choices=[(1, 'Gobierno Regional'), (2, 'Municipalidad'), (3, 'No sabría responder')], help_text='Infraestructura', verbose_name='Infraestructura'),
        ),
        migrations.AlterField(
            model_name='preguntatres',
            name='iniciativa_3',
            field=models.IntegerField(choices=[(1, 'Gobierno Regional'), (2, 'Municipalidad'), (3, 'No sabría responder')], help_text='Servicios o beneficios sociales', verbose_name='Servicios o beneficios sociales'),
        ),
        migrations.AlterField(
            model_name='preguntatres',
            name='iniciativa_4',
            field=models.IntegerField(choices=[(1, 'Gobierno Regional'), (2, 'Municipalidad'), (3, 'No sabría responder')], help_text='Económicas', verbose_name='Económicas'),
        ),
        migrations.AlterField(
            model_name='preguntatres',
            name='iniciativa_5',
            field=models.IntegerField(choices=[(1, 'Gobierno Regional'), (2, 'Municipalidad'), (3, 'No sabría responder')], help_text='Ordenamiento del territorio', verbose_name='Ordenamiento del territorio'),
        ),
    ]