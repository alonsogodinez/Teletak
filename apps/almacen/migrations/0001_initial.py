# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ubicacion', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='DetalleAlmacen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('serie', models.CharField(max_length=20, null=True, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('unidad_caja', models.IntegerField(null=True, blank=True)),
                ('estado', models.CharField(max_length=15, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSalida',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('guia_remision', models.CharField(max_length=20, null=True, blank=True)),
                ('dni_usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.AutoField(max_length=10, serialize=False, primary_key=True)),
                ('sap', models.CharField(max_length=10, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=50, null=True, blank=True)),
                ('categoria', models.CharField(max_length=10, null=True, blank=True)),
                ('stock_minimo', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equiv', models.DecimalField(verbose_name=b'Equivalencia', max_digits=4, decimal_places=2)),
                ('prod', models.ForeignKey(to='almacen.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('nodo', models.CharField(max_length=15, null=True, blank=True)),
                ('devolucion', models.NullBooleanField()),
                ('dni_usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('id_almacen', models.ForeignKey(to='almacen.Almacen')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedicion',
            fields=[
                ('id_und', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='productomedida',
            name='unidad',
            field=models.ForeignKey(to='almacen.UnidadMedicion'),
        ),
        migrations.AddField(
            model_name='detallesalida',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
        migrations.AddField(
            model_name='detallesalida',
            name='id_salida',
            field=models.ForeignKey(blank=True, to='almacen.Salida', null=True),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='id_ingreso',
            field=models.ForeignKey(blank=True, to='almacen.Ingreso', null=True),
        ),
        migrations.AddField(
            model_name='detallealmacen',
            name='codigo_producto',
            field=models.ForeignKey(to='almacen.Producto'),
        ),
        migrations.AddField(
            model_name='detallealmacen',
            name='id_almacen',
            field=models.ForeignKey(to='almacen.Almacen'),
        ),
        migrations.AddField(
            model_name='detallealmacen',
            name='id_ingreso',
            field=models.ForeignKey(blank=True, to='almacen.Ingreso', null=True),
        ),
    ]
