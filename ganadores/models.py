from django.db import models

# Create your models here.
class Ganador(models.Model):
    DEPARTAMENTOS = (
        (0, 'Ninguno'),
        (1, 'Atlántida'),
        (2, 'Choluteca'),
        (3, 'Colón'),
        (4, 'Comayagua'),
        (5, 'Copán'),
        (6, 'Cortes'),
        (7, 'El Paraíso'),
        (8, 'Francisco Morazán'),
        (9, 'Gracias a Dios'),
        (10, 'Intibucá'),
        (11, 'Islas de la Bahía'),
        (12, 'La Paz'),
        (13, 'Lempira'),
        (14, 'Ocotepeque'),
        (15, 'Olancho'),
        (16, 'Santa Bárbara'),
        (17, 'Valle'),
        (18, 'Yoro'),
    )

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    departamento_id = models.IntegerField(default=0, choices=DEPARTAMENTOS)

    fecha_creado = models.DateTimeField('Fecha Creado', auto_now_add=True)

    def __str__(self):  # __unicode__ on Python
        return self.nombre + " " + self.apellido