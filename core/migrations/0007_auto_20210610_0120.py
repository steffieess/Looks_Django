# Generated by Django 3.2.4 on 2021-06-10 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_direccion_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('idCatalogo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Catalogo')),
                ('nCategoria', models.CharField(max_length=30, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idCiudad', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Ciudad')),
                ('nCiudad', models.CharField(max_length=30, verbose_name='Nombre Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Region')),
                ('nRegion', models.CharField(max_length=30, verbose_name='Nombre Region')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEnvio',
            fields=[
                ('idEnvio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Envio')),
                ('tEnvio', models.CharField(max_length=30, verbose_name='Tipo Envio')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('idPago', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Tipo Pago')),
                ('tPago', models.CharField(max_length=30, verbose_name='Tipo Pago')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idTipo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Tipo Usuario')),
                ('nombreus', models.CharField(max_length=20, verbose_name='Nombre Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('idTienda', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Tienda')),
                ('nTienda', models.CharField(max_length=30, verbose_name='Nombre Tienda')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('nProducto', models.CharField(max_length=30, verbose_name='Nombre del Producto')),
                ('stock', models.CharField(max_length=15, verbose_name='Info Stock')),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('idOrden', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Orden')),
                ('fcompra', models.DateField(max_length=30, verbose_name='Fecha de Compra')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('iva', models.IntegerField(verbose_name='IVA')),
                ('comentario', models.CharField(blank=True, max_length=100, verbose_name='Comentario de Compra')),
                ('tipoenvio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoenvio')),
                ('tipopago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipopago')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('idDetalle', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Detalle')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad Total')),
                ('subtotal', models.IntegerField(verbose_name='SubTotal')),
                ('ordencompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordencompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Comentario')),
                ('comentario', models.CharField(max_length=100, verbose_name='Comentario')),
                ('fcomentario', models.DateField(verbose_name='Fecha del Comentario')),
                ('calificacion', models.CharField(max_length=10, verbose_name='Calificación')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ciudad'),
        ),
        migrations.AddField(
            model_name='user',
            name='tipousuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario'),
        ),
    ]
