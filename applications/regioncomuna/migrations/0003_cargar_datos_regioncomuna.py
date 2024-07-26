# Generated by Django 4.2.2 on 2024-05-17 16:36

from django.db import migrations
import json

def cargar_datos_regioncomuna(apps, schema_editor):
    # Import the model using the historical version
    Region = apps.get_model('regioncomuna', 'Region')
    Comuna = apps.get_model('regioncomuna', 'Comuna')
    
    # Cargar los datos desde el archivo JSON
    with open('regioncomuna.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for region_data in data['regiones']:
            region, created = Region.objects.get_or_create(
                region=region_data['region'])
            for comuna_data in region_data['comunas']:
                Comuna.objects.create(comuna=comuna_data, region=region)

class Migration(migrations.Migration):

    dependencies = [
        ('regioncomuna', '0002_rename_nombre_comuna_comuna_and_more'),  # Cambia 'previous_migration_name' por el nombre de la última migración
    ]

    operations = [
        migrations.RunPython(cargar_datos_regioncomuna),
    ]