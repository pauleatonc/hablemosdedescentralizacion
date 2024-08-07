from django.db import models
from django.core.exceptions import ValidationError


class PreguntaUno(models.Model):
    VALORES = (
        ('1', 'No es importante'),
        ('2', 'Algo importante'),
        ('3', 'Importante'),
        ('4', 'Muy importante'),
        ('5', 'No sabría responder'),
    )

    valor = models.CharField(
        max_length=1, choices=VALORES, verbose_name='Valor')
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 1: ¿Qué valor le otorga usted a la descentralización en la cotidianeidad y en la ' \
                       'calidad de vida de las personas?'
        unique_together = ('usuario',)


class PreguntaDos(models.Model):
    VALORACION = (
        (1, '1: Poco prioritario'),
        (2, '2: Algo prioritario'),
        (3, '3: Prioritario'),
        (4, '4: Muy prioritario'),
        (5, 'No sabría responder'),
    )

    propuesta_1 = models.IntegerField(verbose_name='Rendimiento de cuentas', choices=VALORACION,
                                     help_text='Que las autoridades elegidas directamente, rindan cuenta a la ciudadanía.')

    propuesta_2 = models.IntegerField(verbose_name='Acceso a bienes y prestación de servicios', choices=VALORACION,
                                     help_text='Que la ciudadanía tenga acceso a bienes y prestaciones de servicios públicos, que hoy entrega el gobierno central, a través de los gobiernos regionales y municipalidades.')

    propuesta_3 = models.IntegerField(verbose_name='Mayores recursos públicos', choices=VALORACION,
                                     help_text='Que los gobiernos regionales y municipalidades cuenten con mayores recursos financieros, y sus usos sean definidos en el territorio.')

    propuesta_4 = models.IntegerField(verbose_name='Más profesionales,', choices=VALORACION,
                                     help_text='Que los gobiernos regionales y municipalidades cuenten con más profesionales, para el cumplimiento de sus objetivos.')

    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 2: Impacto de la descentralización en las personas y comunidades.'
        unique_together = ('usuario',)


class PreguntaTres(models.Model):
    ITEMS = (
        (1, 'Gobierno Regional'),
        (2, 'Municipalidad'),
        (3, 'Ambas'),
        (4, 'No sabría responder')
    )

    iniciativa_1 = models.IntegerField(verbose_name='Iniciativas ambientales', choices=ITEMS,
                                       help_text='Iniciativas ambientales')
    iniciativa_2 = models.IntegerField(verbose_name='Infraestructura pública', choices=ITEMS,
                                       help_text='Infraestructura pública')
    iniciativa_3 = models.IntegerField(verbose_name='Servicios o beneficios sociales', choices=ITEMS,
                                       help_text='Servicios o beneficios sociales')
    iniciativa_4 = models.IntegerField(verbose_name='Fomento productivo', choices=ITEMS,
                                       help_text='Fomento productivo')
    iniciativa_5 = models.IntegerField(verbose_name='Ordenamiento del territorio', choices=ITEMS,
                                       help_text='Ordenamiento del territorio')
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 3: Iniciativas que podrían ser incluidas dentro de la Política Nacional de ' \
                       'Descentralización.'
        unique_together = ('usuario',)


class OpcionesPreguntaCinco(models.Model):
    clave = models.CharField(max_length=2)
    texto = models.TextField()

    def __str__(self):
        return self.texto
    

class PreguntaCinco(models.Model):
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)
    opciones = models.ManyToManyField(OpcionesPreguntaCinco, verbose_name='Selecciona tres opciones')

    class Meta:
        verbose_name = 'Pregunta 5: Para usted ¿cuáles de las siguientes medidas preferiría que fuesen implementadas por una Política de Descentralización de Chile? Marcar tres alternativas.'
        unique_together = ('usuario',)

    def get_opciones_texto(self):
        return [opcion.texto for opcion in self.opciones.all()]


class PreguntaSeis(models.Model):
    VALORES = (
        ('1', 'Mejorará la calidad de vida de las personas.'),
        ('2', 'Mantendrá de igual manera la calidad de vida de las personas.'),
        ('3', 'Generará un retroceso en la calidad de vida de las personas.'),
        ('4', 'No sabría responder'),
    )

    valor = models.CharField(
        max_length=1, choices=VALORES, verbose_name='Valor')
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 6: Considerando que una Política de Descentralización de Chile contaría con una agenda de trabajo con un plazo de implementación a 10 años, ¿con cuál de las siguientes alternativas usted está más de acuerdo?'
        unique_together = ('usuario',)


class PreguntaSiete(models.Model):
    texto_respuesta = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 7: Para finalizar y considerando sus respuestas anteriores, ¿qué temática o medida agregaría, para serconsiderada en una Política de Descentralización de Chile? Esta pregunta es opcional.'
        unique_together = ('usuario',)