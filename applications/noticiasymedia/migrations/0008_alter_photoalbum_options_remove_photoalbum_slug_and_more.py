# Generated by Django 4.2.2 on 2024-07-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticiasymedia', '0007_photoalbum_date_alter_photoalbum_foto_portada_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoalbum',
            options={'ordering': ['region__region']},
        ),
        migrations.RemoveField(
            model_name='photoalbum',
            name='slug',
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='titulo_album',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo Album (obligatorio)'),
        ),
    ]
