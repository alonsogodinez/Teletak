# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20150614_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='productomedida',
            name='prod',
        ),
        migrations.RemoveField(
            model_name='productomedida',
            name='unidad',
        ),
        migrations.AddField(
            model_name='almacen',
            name='capacidad',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='detallealmacen',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='productos.Producto', null=True),
        ),
        migrations.AlterField(
            model_name='detallealmacen',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='detalleingreso',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='productos.Producto', null=True),
        ),
        migrations.AlterField(
            model_name='detalleingreso',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='detallesalida',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='productos.Producto', null=True),
        ),
        migrations.AlterField(
            model_name='detallesalida',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='salida',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='ProductoMedida',
        ),
        migrations.DeleteModel(
            name='UnidadMedicion',
        ),
    ]
