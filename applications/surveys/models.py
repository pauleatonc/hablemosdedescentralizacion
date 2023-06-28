from django.db import models


class PreguntaUno(models.Model):
    VALORES = (
        ('1', 'Es muy importante'),
        ('2', 'Es importante'),
        ('3', 'Es poco importante'),
        ('4', 'No es importante'),
        ('5', 'No sabría responder'),
    )

    valor = models.CharField(max_length=1, choices=VALORES)

    class Meta:
        verbose_name = '¿Qué valor le otorga usted a la descentralización en la cotidianeidad y en la calidad de ' \
                       'vida de las personas?'


class PreguntaDos(models.Model):
    ITEMS = (
        (1, 'La descentralización permite tomar decisiones, a partir de las características, conocimientos y '
            'experiencias de los territorios y sus comunidades.'),
        (2, 'La descentralización permite fortalecer la democracia a nivel de regiones y comunas.'),
        (3, 'La descentralización permite satisfacer necesidades de manera oportuna y eficiente.'),
        (4, 'La descentralización permite disminuir las desigualdades sociales y territoriales.'),
    )

    prioridad_1 = models.IntegerField(choices=ITEMS)
    prioridad_2 = models.IntegerField(choices=ITEMS)
    prioridad_3 = models.IntegerField(choices=ITEMS)
    prioridad_4 = models.IntegerField(choices=ITEMS)

    def clean(self):
        # Verificar que los valores de los ítems no se repitan
        items = [self.prioridad_1, self.prioridad_2, self.prioridad_3, self.prioridad_4]
        if len(set(items)) < len(items):
            raise models.ValidationError("Los valores de los ítems no pueden repetirse.")

    class Meta:
        verbose_name = 'Impacto de la descentralización en las personas y comunidades.'


class PreguntaTres(models.Model):
    ITEMS = (
        (1, 'Establecer mecanismos de participación ciudadana y rendición de cuentas.'),
        (2, 'Establecer qué le corresponde institucionalmente realizar a los distintos niveles de la administración '
            'pública, nacional, regional y comunal.'),
        (3, 'Garantizar la autonomía y el buen uso de los recursos financieros públicos.'),
        (4, 'Coordinar a distintos actores públicos, privados y sociales, para la mejor obtención de objetivos de '
            'desarrollo.'),
        (5, 'Fortalecer capacidades técnicas y profesionales en comunas y regiones, para generar mayores oportunidades '
            'de desarrollo económico, social y cultural.'),
    )

    prioridad_1 = models.IntegerField(choices=ITEMS)
    prioridad_2 = models.IntegerField(choices=ITEMS)
    prioridad_3 = models.IntegerField(choices=ITEMS)
    prioridad_4 = models.IntegerField(choices=ITEMS)
    prioridad_5 = models.IntegerField(choices=ITEMS)

    def clean(self):
        # Verificar que los valores de los ítems no se repitan
        items = [self.prioridad_1, self.prioridad_2, self.prioridad_3, self.prioridad_4, self.prioridad_5]
        if len(set(items)) < len(items):
            raise models.ValidationError("Los valores de los ítems no pueden repetirse.")

    class Meta:
        verbose_name = 'Iniciativas que podrían ser incluidas dentro de la Política Nacional de Descentralización.'


class PreguntaCinco(models.Model):
    texto_respuesta = models.TextField()

    class Meta:
        verbose_name = '¿Qué tema, iniciativa o aspecto profundizaría o agregaría, considerando el vínculo entre ' \
                       'descentralización y su vida personal y en comunidad?'


class Respuesta(models.Model):
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)
    pregunta_uno = models.ForeignKey(PreguntaUno, on_delete=models.CASCADE, null=True)
    pregunta_dos = models.ForeignKey(PreguntaDos, on_delete=models.CASCADE, null=True)
    pregunta_tres = models.ForeignKey(PreguntaTres, on_delete=models.CASCADE, null=True)
    pregunta_cinco = models.ForeignKey(PreguntaCinco, on_delete=models.CASCADE, null=True, blank=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario',)