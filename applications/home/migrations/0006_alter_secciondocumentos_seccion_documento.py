# Generated by Django 4.2.2 on 2023-07-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_documentos_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secciondocumentos',
            name='seccion_documento',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
