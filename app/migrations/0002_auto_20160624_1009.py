# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 13:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testevelocidadefixa',
            name='testeVF_velocidade',
            field=models.FloatField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Velocidade do Motor'),
        ),
    ]
