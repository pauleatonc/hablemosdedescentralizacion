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
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 1: ¿Qué valor le otorga usted a la descentralización en la cotidianeidad y en la ' \
                       'calidad de vida de las personas?'
        unique_together = ('usuario',)


class PreguntaDos(models.Model):
    ITEMS = (
        (1, 'Prioridad 1'),
        (2, 'Prioridad 2'),
        (3, 'Prioridad 3'),
        (4, 'Prioridad 4'),
    )

    propuesta_1 = models.IntegerField(choices=ITEMS,
                                      help_text='La descentralización permite tomar decisiones, a partir de las '
                                                'características, conocimientos y experiencias de los territorios y '
                                                'sus comunidades.')
    propuesta_2 = models.IntegerField(choices=ITEMS,
                                      help_text='La descentralización permite fortalecer la democracia a nivel de '
                                                'regiones y comunas.')
    propuesta_3 = models.IntegerField(choices=ITEMS,
                                      help_text='La descentralización permite satisfacer necesidades de manera '
                                                'oportuna y eficiente.')
    propuesta_4 = models.IntegerField(choices=ITEMS,
                                      help_text='La descentralización permite disminuir las desigualdades sociales y '
                                                'territoriales.')
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def clean(self):
        # Verificar que los valores de los ítems no se repitan
        items = [self.propuesta_1, self.propuesta_2, self.propuesta_3, self.propuesta_4]
        if len(set(items)) < len(items):
            raise models.ValidationError("Los valores de los ítems no pueden repetirse.")

    class Meta:
        verbose_name = 'Pregunta 2: Impacto de la descentralización en las personas y comunidades.'
        unique_together = ('usuario',)


class PreguntaTres(models.Model):
    ITEMS = (
        (1, 'Prioridad 1'),
        (2, 'Prioridad 2'),
        (3, 'Prioridad 3'),
        (4, 'Prioridad 4'),
        (5, 'Prioridad 5'),
    )

    iniciativa_1 = models.IntegerField(choices=ITEMS,
                                      help_text='Establecer mecanismos de participación ciudadana y rendición de '
                                                'cuentas.')
    iniciativa_2 = models.IntegerField(choices=ITEMS,
                                      help_text='Establecer qué le corresponde institucionalmente realizar a los '
                                                'distintos niveles de la administración pública, nacional, regional y '
                                                'comunal.')
    iniciativa_3 = models.IntegerField(choices=ITEMS,
                                      help_text='Garantizar la autonomía y el buen uso de los recursos financieros '
                                                'públicos.')
    iniciativa_4 = models.IntegerField(choices=ITEMS,
                                      help_text='Coordinar a distintos actores públicos, privados y sociales, para la '
                                                'mejor obtención de objetivos de desarrollo.')
    iniciativa_5 = models.IntegerField(choices=ITEMS,
                                      help_text='Fortalecer capacidades técnicas y profesionales en comunas y regiones, '
                                                'para generar mayores oportunidades de desarrollo económico, social y '
                                                'cultural.')
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def clean(self):
        # Verificar que los valores de los ítems no se repitan
        items = [self.iniciativa_1, self.iniciativa_2, self.iniciativa_3, self.iniciativa_4, self.iniciativa_5]
        if len(set(items)) < len(items):
            raise models.ValidationError("Los valores de los ítems no pueden repetirse.")

    class Meta:
        verbose_name = 'Pregunta 3: Iniciativas que podrían ser incluidas dentro de la Política Nacional de ' \
                       'Descentralización.'
        unique_together = ('usuario',)


class PreguntaCinco(models.Model):
    texto_respuesta = models.TextField(blank=True)
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 5: ¿Qué tema, iniciativa o aspecto profundizaría o agregaría, considerando el ' \
                       'vínculo entre descentralización y su vida personal y en comunidad?'
        unique_together = ('usuario',)