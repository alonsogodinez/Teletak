# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150519_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(max_length=8, null=True, verbose_name=b'Dni'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cellphone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name=b'Apellido'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Telefono', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=b'TRA', max_length=10, verbose_name=b'tipo de usuario', choices=[(b'TRA', b'Trabajador'), (b'GER', b'Gerente')]),
        ),
    ]
