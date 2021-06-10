from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Catalogo, Ciudad, Comentario, DetalleCompra, OrdenCompra, Producto, Region, Tienda, TipoEnvio, TipoPago, Tipous, Persona, Direccion


# Register your models here.
admin.site.register(Persona)
admin.site.register(Direccion)
admin.site.register(Tienda)
admin.site.register(Comentario)
admin.site.register(TipoEnvio)
admin.site.register(TipoPago)
admin.site.register(Tipous)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Catalogo)
admin.site.register(Producto)
admin.site.register(OrdenCompra)
admin.site.register(DetalleCompra)

