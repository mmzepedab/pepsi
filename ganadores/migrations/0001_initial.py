# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ganador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200)),
                ('departamento_id', models.IntegerField(choices=[(0, 'Ninguno'), (1, 'Atlántida'), (2, 'Choluteca'), (3, 'Colón'), (4, 'Comayagua'), (5, 'Copán'), (6, 'Cortes'), (7, 'El Paraíso'), (8, 'Francisco Morazán'), (9, 'Gracias a Dios'), (10, 'Intibucá'), (11, 'Islas de la Bahía'), (12, 'La Paz'), (13, 'Lempira'), (14, 'Ocotepeque'), (15, 'Olancho'), (16, 'Santa Bárbara'), (17, 'Valle'), (18, 'Yoro')], default=0)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creado')),
            ],
        ),
    ]