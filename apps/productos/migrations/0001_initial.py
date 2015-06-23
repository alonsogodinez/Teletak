# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.AutoField(max_length=10, serialize=False, primary_key=True)),
                ('sap', models.CharField(max_length=10, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=50, null=True, blank=True)),
                ('stock_minimo', models.IntegerField(null=True, blank=True)),
                ('categoria', models.ForeignKey(blank=True, to='productos.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equivalencia', models.DecimalField(verbose_name=b'Equivalencia', max_digits=4, decimal_places=2)),
                ('codigo_producto', models.ForeignKey(blank=True, to='productos.Producto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='productomedida',
            name='id_unidad',
            field=models.ForeignKey(blank=True, to='productos.UnidadMedicion', null=True),
        ),
    ]
