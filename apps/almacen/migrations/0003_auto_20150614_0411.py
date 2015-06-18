# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('almacen', '0002_auto_20150614_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='dni_usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, to='almacen.Categoria', null=True),
        ),
        migrations.AddField(
            model_name='productomedida',
            name='prod',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
        migrations.AddField(
            model_name='productomedida',
            name='unidad',
            field=models.ForeignKey(blank=True, to='almacen.UnidadMedicion', null=True),
        ),
        migrations.AddField(
            model_name='salida',
            name='dni_usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='salida',
            name='id_almacen',
            field=models.ForeignKey(blank=True, to='almacen.Almacen', null=True),
        ),
    ]
