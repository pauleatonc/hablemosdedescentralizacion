# Generated by Django 4.2.2 on 2023-07-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0010_alter_preguntados_propuesta_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntacinco',
            name='texto_respuesta',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]