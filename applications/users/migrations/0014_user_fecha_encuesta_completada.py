# Generated by Django 4.2.2 on 2024-06-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_familiaridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fecha_encuesta_completada',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]