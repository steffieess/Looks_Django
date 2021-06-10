from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User (models.Model):
    nDocumento = models.IntegerField(primary_key=True, verbose_name='Numero de Documento')
    nombre = models.CharField(max_length=20, verbose_name='Nombre', blank=False)
    appaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    apmaterno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    email = models.CharField(max_length=60, verbose_name='Email', blank=False)
    telefono = models.CharField(max_length=15, verbose_name='Telefono', blank=False)
    password = models.CharField(max_length=15, verbose_name='Clave', blank=False)

    def __str__(self):
        return self.nombre

class Direccion (models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id Direccion')
    calle = models.CharField(max_length=30, verbose_name='Nombre Calle', blank=False)
    tipoVivienda = models.CharField(max_length=15, verbose_name='Casa o Depto', blank=False)
    numero = models.CharField(max_length=10, verbose_name='Numero o Letra', blank=False )
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.tipoVivienda

class Comentario (models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id Direccion')
    calle = models.CharField(max_length=30, verbose_name='Nombre Calle', blank=False)
    tipoVivienda = models.CharField(max_length=15, verbose_name='Casa o Depto', blank=False)
    numero = models.CharField(max_length=10, verbose_name='Numero o Letra', blank=False )
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.tipoVivienda




    
