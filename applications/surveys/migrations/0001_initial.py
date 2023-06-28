# Generated by Django 4.2.2 on 2023-06-28 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntaCinco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.TextField()),
            ],
            options={
                'verbose_name': '¿Qué tema, iniciativa o aspecto profundizaría o agregaría, considerando el vínculo entre descentralización y su vida personal y en comunidad?',
            },
        ),
        migrations.CreateModel(
            name='PreguntaDos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridad_1', models.IntegerField(choices=[(1, 'La descentralización permite tomar decisiones, a partir de las características, conocimientos y experiencias de los territorios y sus comunidades.'), (2, 'La descentralización permite fortalecer la democracia a nivel de regiones y comunas.'), (3, 'La descentralización permite satisfacer necesidades de manera oportuna y eficiente.'), (4, 'La descentralización permite disminuir las desigualdades sociales y territoriales.')])),
                ('prioridad_2', models.IntegerField(choices=[(1, 'La descentralización permite tomar decisiones, a partir de las características, conocimientos y experiencias de los territorios y sus comunidades.'), (2, 'La descentralización permite fortalecer la democracia a nivel de regiones y comunas.'), (3, 'La descentralización permite satisfacer necesidades de manera oportuna y eficiente.'), (4, 'La descentralización permite disminuir las desigualdades sociales y territoriales.')])),
                ('prioridad_3', models.IntegerField(choices=[(1, 'La descentralización permite tomar decisiones, a partir de las características, conocimientos y experiencias de los territorios y sus comunidades.'), (2, 'La descentralización permite fortalecer la democracia a nivel de regiones y comunas.'), (3, 'La descentralización permite satisfacer necesidades de manera oportuna y eficiente.'), (4, 'La descentralización permite disminuir las desigualdades sociales y territoriales.')])),
                ('prioridad_4', models.IntegerField(choices=[(1, 'La descentralización permite tomar decisiones, a partir de las características, conocimientos y experiencias de los territorios y sus comunidades.'), (2, 'La descentralización permite fortalecer la democracia a nivel de regiones y comunas.'), (3, 'La descentralización permite satisfacer necesidades de manera oportuna y eficiente.'), (4, 'La descentralización permite disminuir las desigualdades sociales y territoriales.')])),
            ],
            options={
                'verbose_name': 'Impacto de la descentralización en las personas y comunidades.',
            },
        ),
        migrations.CreateModel(
            name='PreguntaTres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridad_1', models.IntegerField(choices=[(1, 'Establecer mecanismos de participación ciudadana y rendición de cuentas.'), (2, 'Establecer qué le corresponde institucionalmente realizar a los distintos niveles de la administración pública, nacional, regional y comunal.'), (3, 'Garantizar la autonomía y el buen uso de los recursos financieros públicos.'), (4, 'Coordinar a distintos actores públicos, privados y sociales, para la mejor obtención de objetivos de desarrollo.'), (5, 'Fortalecer capacidades técnicas y profesionales en comunas y regiones, para generar mayores oportunidades de desarrollo económico, social y cultural.')])),
                ('prioridad_2', models.IntegerField(choices=[(1, 'Establecer mecanismos de participación ciudadana y rendición de cuentas.'), (2, 'Establecer qué le corresponde institucionalmente realizar a los distintos niveles de la administración pública, nacional, regional y comunal.'), (3, 'Garantizar la autonomía y el buen uso de los recursos financieros públicos.'), (4, 'Coordinar a distintos actores públicos, privados y sociales, para la mejor obtención de objetivos de desarrollo.'), (5, 'Fortalecer capacidades técnicas y profesionales en comunas y regiones, para generar mayores oportunidades de desarrollo económico, social y cultural.')])),
                ('prioridad_3', models.IntegerField(choices=[(1, 'Establecer mecanismos de participación ciudadana y rendición de cuentas.'), (2, 'Establecer qué le corresponde institucionalmente realizar a los distintos niveles de la administración pública, nacional, regional y comunal.'), (3, 'Garantizar la autonomía y el buen uso de los recursos financieros públicos.'), (4, 'Coordinar a distintos actores públicos, privados y sociales, para la mejor obtención de objetivos de desarrollo.'), (5, 'Fortalecer capacidades técnicas y profesionales en comunas y regiones, para generar mayores oportunidades de desarrollo económico, social y cultural.')])),
                ('prioridad_4', models.IntegerField(choices=[(1, 'Establecer mecanismos de participación ciudadana y rendición de cuentas.'), (2, 'Establecer qué le corresponde institucionalmente realizar a los distintos niveles de la administración pública, nacional, regional y comunal.'), (3, 'Garantizar la autonomía y el buen uso de los recursos financieros públicos.'), (4, 'Coordinar a distintos actores públicos, privados y sociales, para la mejor obtención de objetivos de desarrollo.'), (5, 'Fortalecer capacidades técnicas y profesionales en comunas y regiones, para generar mayores oportunidades de desarrollo económico, social y cultural.')])),
                ('prioridad_5', models.IntegerField(choices=[(1, 'Establecer mecanismos de participación ciudadana y rendición de cuentas.'), (2, 'Establecer qué le corresponde institucionalmente realizar a los distintos niveles de la administración pública, nacional, regional y comunal.'), (3, 'Garantizar la autonomía y el buen uso de los recursos financieros públicos.'), (4, 'Coordinar a distintos actores públicos, privados y sociales, para la mejor obtención de objetivos de desarrollo.'), (5, 'Fortalecer capacidades técnicas y profesionales en comunas y regiones, para generar mayores oportunidades de desarrollo económico, social y cultural.')])),
            ],
            options={
                'verbose_name': 'Iniciativas que podrían ser incluidas dentro de la Política Nacional de Descentralización.',
            },
        ),
        migrations.CreateModel(
            name='PreguntaUno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(choices=[('1', 'Es muy importante'), ('2', 'Es importante'), ('3', 'Es poco importante'), ('4', 'No es importante'), ('5', 'No sabría responder')], max_length=1)),
            ],
            options={
                'verbose_name': '¿Qué valor le otorga usted a la descentralización en la cotidianeidad y en la calidad de vida de las personas?',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('pregunta_cinco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.preguntacinco')),
                ('pregunta_dos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.preguntados')),
                ('pregunta_tres', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.preguntatres')),
                ('pregunta_uno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.preguntauno')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
