# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallealmacen',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
        migrations.AddField(
            model_name='detallealmacen',
            name='id_almacen',
            field=models.ForeignKey(blank=True, to='almacen.Almacen', null=True),
        ),
        migrations.AddField(
            model_name='detallealmacen',
            name='id_ingreso',
            field=models.ForeignKey(blank=True, to='almacen.Ingreso', null=True),
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
            model_name='detallesalida',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
        migrations.AddField(
            model_name='detallesalida',
            name='id_salida',
            field=models.ForeignKey(blank=True, to='almacen.Salida', null=True),
        ),
    ]
