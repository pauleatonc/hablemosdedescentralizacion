# Generated by Django 4.2.2 on 2023-07-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticiasymedia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multimedia',
            old_name='tag_media',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='tag_noticia',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='autor',
            field=models.CharField(blank=True, max_length=100, verbose_name='autor (opcional)'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='autor',
            field=models.CharField(blank=True, max_length=100, verbose_name='autor (opcional)'),
        ),
    ]
