# Generated by Django 4.2.2 on 2023-07-19 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticiasymedia', '0003_noticias_galeria_url_alter_multimedia_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, max_length=300),
            preserve_default=False,
        ),
    ]
