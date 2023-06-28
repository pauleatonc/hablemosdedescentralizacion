from django.db import models


class PreguntaUno(models.Model):
    VALORES = (
        ('1', 'Es muy importante'),
        ('2', 'Es importante'),
        ('3', 'Es poco importante'),
        ('4', 'No es importante'),
        ('5', 'No sabría responder'),
    )

    pregunta = models.TextField()
    valor = models.CharField(max_length=1, choices=VALORES)


class PreguntaDos(models.Model):
    ITEMS = (
        (1, 'La descentralización permite tomar decisiones, a partir de las características, conocimientos y '
            'experiencias de los territorios y sus comunidades.'),
        (2, 'La descentralización permite fortalecer la democracia a nivel de regiones y comunas.'),
        (3, 'La descentralización permite satisfacer necesidades de manera oportuna y eficiente.'),
        (4, 'La descentralización permite disminuir las desigualdades sociales y territoriales.'),
    )

    pregunta = models.TextField()
    item_1 = models.IntegerField(choices=ITEMS)
    item_2 = models.IntegerField(choices=ITEMS)
    item_3 = models.IntegerField(choices=ITEMS)
    item_4 = models.IntegerField(choices=ITEMS)

    def clean(self):
        # Verificar que los valores de los ítems no se repitan
        items = [self.item_1, self.item_2, self.item_3, self.item_4]
        if len(set(items)) < len(items):
            raise models.ValidationError("Los valores de los ítems no pueden repetirse.")


class Respuesta(models.Model):
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)
    pregunta_uno = models.ForeignKey(PreguntaUno, on_delete=models.CASCADE)
    pregunta_dos = models.ForeignKey(PreguntaDos, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)