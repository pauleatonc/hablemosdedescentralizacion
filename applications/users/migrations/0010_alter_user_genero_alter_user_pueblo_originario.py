# Generated by Django 4.2.2 on 2023-07-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_pueblos_originarios_user_pueblo_originario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='genero',
            field=models.CharField(blank=True, choices=[('', 'Elige una opción'), ('FEM', 'Femenino'), ('MASC', 'Masculino'), ('NOBIN', 'No binarie'), ('PND', 'Prefiero no decirlo')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pueblo_originario',
            field=models.CharField(blank=True, choices=[('', 'Elige una opción'), ('NP', 'No pertenece'), ('AIM', 'Aimara'), ('ATAC', 'Atacameño o Lickanantay'), ('COLL', 'Colla'), ('CHAN', 'Chango'), ('DIAG', 'Diaguita'), ('KAW', 'Kawésqar'), ('MAPU', 'Mapuche'), ('QUEC', 'Quechua'), ('RAPA', 'Rapa-Nui'), ('YAG', 'Yagán'), ('OTRO', 'Otro')], max_length=5, null=True),
        ),
    ]
