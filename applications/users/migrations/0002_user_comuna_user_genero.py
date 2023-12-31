# Generated by Django 4.2.2 on 2023-06-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regioncomuna', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comuna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regioncomuna.comuna', verbose_name='Comuna'),
        ),
        migrations.AddField(
            model_name='user',
            name='genero',
            field=models.CharField(choices=[('FEM', 'Femenino'), ('MASC', 'Masculino'), ('NOBIN', 'No binarie'), ('PND', 'Prefiero no decirlo')], default='PND', max_length=5),
        ),
    ]
