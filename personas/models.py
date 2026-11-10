from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    no_calle = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.calle} {self.no_calle} {self.pais}'


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
