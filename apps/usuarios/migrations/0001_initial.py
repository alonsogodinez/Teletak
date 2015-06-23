# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('cellphone', models.CharField(max_length=15, null=True, verbose_name=b'Celular', blank=True)),
                ('dni', models.CharField(max_length=8, null=True, verbose_name=b'Dni')),
                ('email', models.EmailField(max_length=30)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'Nombres')),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Apellidos')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name=b'Telefono', blank=True)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('user_type', models.CharField(default=b'TRA', max_length=10, verbose_name=b'tipo de usuario', choices=[(b'TRA', b'Trabajador'), (b'GER', b'Gerente')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
