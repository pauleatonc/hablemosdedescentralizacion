# Generated by Django 4.2.2 on 2023-07-07 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_documentos_titulo_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='countdown',
            name='start_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
