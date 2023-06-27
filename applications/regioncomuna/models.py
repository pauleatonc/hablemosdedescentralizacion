from django.db import models
import json

# Para cargar el json debes seguir los siguientes pasos en la terminal:
# python manage.py shell
# from applications.regioncomuna.models import Region, Comuna
# from applications.regioncomuna.models import cargar_datos_regioncomuna
# cargar_datos_regioncomuna()

def cargar_datos_regioncomuna():
    with open('regioncomuna.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for region_data in data['regiones']:
            region, created = Region.objects.get_or_create(
                region=region_data['region'])
            for comuna_data in region_data['comunas']:
                Comuna.objects.create(comuna=comuna_data, region=region)


class Region(models.Model):
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region


class Comuna(models.Model):
    comuna = models.CharField(max_length=100)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='comunas')
    
    def __str__(self):
        return self.comuna