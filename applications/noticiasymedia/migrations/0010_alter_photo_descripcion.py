# Generated by Django 4.2.2 on 2024-07-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticiasymedia', '0009_alter_photoalbum_date_alter_photoalbum_public_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion Foto (obligatorio)'),
        ),
    ]