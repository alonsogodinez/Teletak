# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'celular', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'telefono', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(max_length=10, null=True, verbose_name=b'tipo de usuario', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name=b'apellido'),
        ),
    ]
