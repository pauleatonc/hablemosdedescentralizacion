from django.db import models


class PreguntaUno(models.Model):
    VALORES = (
        ('1', 'Es muy importante'),
        ('2', 'Es importante'),
        ('3', 'Es poco importante'),
        ('4', 'No es importante'),
        ('5', 'No sabría responder'),
    )

    valor = models.CharField(max_length=1, choices=VALORES, verbose_name='Valor')
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

    class Meta:
        verbose_name = 'Pregunta 3: Iniciativas que podrían ser incluidas dentro de la Política Nacional de ' \
                       'Descentralización.'
        unique_together = ('usuario',)


class PreguntaCuatro(models.Model):
    VALORACION = (
        (1, 'Muy importante'),
        (2, 'Importante'),
        (3, 'Poco importante'),
        (4, 'No es importante'),
        (5, 'No sabría responder')
    )

    tematica_1 = models.IntegerField(verbose_name='Enfoque de género', choices=VALORACION,
                                      help_text='las medidas deben considerar de manera transversal la perspectiva de '
                                                'género, entendida como una mirada destinada a hacer que las '
                                                'preocupaciones y experiencias de las mujeres, así como las de '
                                                'los hombres y de las diversidades sexo genéricas, sean un elemento '
                                                'integrante de la elaboración de la Política.')

    tematica_2 = models.IntegerField(verbose_name='Diversidad territorial', choices=VALORACION,
                                     help_text='las medidas deben considerar e integrar el respeto a la diversidad '
                                               'territorial en cuanto a las características identitarias de los '
                                               'territorios, su historia, sus características económicas, sociales y '
                                               'culturales, entre otras.')

    tematica_3 = models.IntegerField(verbose_name='Participación ciudadana', choices=VALORACION,
                                     help_text='las medidas y acciones deben promover la participación activa de la '
                                               'sociedad civil en las decisiones de los territorios.')

    tematica_4 = models.IntegerField(verbose_name='Capital humano territorial', choices=VALORACION,
                                     help_text='las medidas deben considerar capacidades técnicas y profesionales para '
                                               'enfrentar los desafíos de desarrollo económico, social y cultural.')

    tematica_5 = models.IntegerField(verbose_name='Protección del medioambiente', choices=VALORACION,
                                     help_text='las medidas deben minimizar su impacto negativo sobre el medio '
                                               'ambiente.')

    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 4: ¿Qué tan importante es incluir las siguientes temáticas de forma transversal en la Política ' \
                       'Nacional de Descentralización?'
        unique_together = ('usuario',)


class PreguntaCinco(models.Model):
    texto_respuesta = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta 5: ¿Qué tema, iniciativa o aspecto profundizaría o agregaría, considerando el ' \
                       'vínculo entre descentralización y su vida personal y en comunidad?'
        unique_together = ('usuario',)