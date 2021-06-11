from enum import Flag
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Tipous (models.Model):
    idTipo= models.IntegerField(primary_key=True, verbose_name='Id Tipo Usuario')
    nombreus = models.CharField(max_length=20, verbose_name='Nombre Usuario', blank=False)

    def __str__(self):
        return self.nombreus

class Persona (models.Model):
    nDocumento = models.IntegerField(primary_key=True, verbose_name='Numero de Documento')
    nombre = models.CharField(max_length=20, verbose_name='Nombre', blank=False)
    appaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno', blank=False)
    apmaterno = models.CharField(max_length=30, verbose_name='Apellido Materno', blank=False)
    email = models.CharField(max_length=60, verbose_name='Email', blank=False)
    telefono = models.IntegerField(verbose_name='Telefono', blank=False)
    password = models.CharField(max_length=15, verbose_name='Clave', blank=False)
    tipous = models.ForeignKey(Tipous,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Region (models.Model):
    idRegion = models.IntegerField(primary_key=True, verbose_name='Id Region')
    nRegion = models.CharField(max_length=30, verbose_name='Nombre Region', blank=False)
        
    def __str__(self):
        return self.nRegion

class Ciudad (models.Model):
    idCiudad = models.IntegerField(primary_key=True, verbose_name='Id Ciudad')
    nCiudad = models.CharField(max_length=30, verbose_name='Nombre Ciudad')
    region = models.ForeignKey(Region,on_delete=models.CASCADE, null=True)
        
    def __str__(self):
        return self.nCiudad

class Direccion (models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id Direccion')
    calle = models.CharField(max_length=30, verbose_name='Nombre Calle')
    tipoVivienda = models.CharField(max_length=15, verbose_name='Casa o Depto')
    numero = models.CharField(max_length=10, verbose_name='Numero o Letra')
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE, null=True)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tipoVivienda

class Tienda (models.Model):
    idTienda = models.IntegerField(primary_key=True, verbose_name='Id Tienda')
    nTienda = models.CharField(max_length=30, verbose_name='Nombre Tienda')
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nTienda

class Catalogo (models.Model):
    idCatalogo= models.IntegerField(primary_key=True, verbose_name='Id Catalogo')
    nCategoria = models.CharField(max_length=30, verbose_name='Categoria', blank=False)
 
    def __str__(self):
        return self.nCategoria

class Producto (models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    nProducto = models.CharField(max_length=30, verbose_name='Nombre del Producto', blank=False)
    stock = models.CharField(max_length=15, verbose_name= 'Info Stock', blank=False)
    catalogo = models.ForeignKey(Catalogo,on_delete=models.CASCADE)

    def __str__(self):
        return self.nProducto

class Comentario (models.Model):
    idComentario = models.IntegerField(primary_key=True, verbose_name='Id Comentario', null=True)
    coment = models.CharField(max_length=50, verbose_name='Comentario', blank=False)
    fcomentario = models.DateField(verbose_name='Fecha del Comentario', blank=False)
    calificacion = models.CharField(max_length=10, verbose_name='Calificación', blank=False)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.coment

class TipoEnvio (models.Model):
    idEnvio = models.IntegerField(primary_key=True, verbose_name='Id Envio')
    tEnvio = models.CharField(max_length=30, verbose_name='Tipo Envio')

    def __str__(self):
        return self.tEnvio

class TipoPago (models.Model):
    idPago = models.IntegerField(primary_key=True, verbose_name='Id Tipo Pago')
    tPago = models.CharField(max_length=30, verbose_name='Tipo Pago')

    def __str__(self):
        return self.tPago

class OrdenCompra (models.Model):
    idOrden = models.IntegerField(primary_key=True, verbose_name='Id Orden')
    fcompra = models.DateField(max_length=30, verbose_name='Fecha de Compra', blank=False)
    total = models.IntegerField(verbose_name='Total', blank=False)
    iva = models.IntegerField(verbose_name='IVA', blank=False )
    comentario = models.CharField(max_length=100, verbose_name='Comentario de Compra', blank=True)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE, null=True)
    tipoenvio = models.ForeignKey(TipoEnvio,on_delete=models.CASCADE)
    tipopago = models.ForeignKey(TipoPago,on_delete=models.CASCADE)

    def __str__(self):
        return self.idOrden

class DetalleCompra (models.Model):
    idDetalle = models.IntegerField(primary_key=True, verbose_name='Id Detalle')
    cantidad = models.IntegerField(verbose_name='Cantidad Total', blank=False)
    subtotal = models.IntegerField(verbose_name='SubTotal', blank=False)
    ordencompra = models.ForeignKey(OrdenCompra,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idDetalle







    
