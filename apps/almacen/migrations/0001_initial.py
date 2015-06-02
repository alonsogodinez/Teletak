# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
            ],
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
            name='GuiaRemision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_traslado', models.DateField()),
                ('punto_partida', models.CharField(max_length=30)),
                ('nro_guia_remitente', models.CharField(max_length=15)),
                ('placa_vehiculo', models.CharField(max_length=10)),
                ('licencia_conducir', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('guia_remision', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.AutoField(max_length=10, serialize=False, primary_key=True)),
                ('sap', models.CharField(max_length=10, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=50, null=True, blank=True)),
                ('stock_minimo', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equiv', models.DecimalField(verbose_name=b'Equivalencia', max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('ruc', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('nodo', models.CharField(max_length=15, null=True, blank=True)),
                ('devolucion', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedicion',
            fields=[
                ('id_und', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
