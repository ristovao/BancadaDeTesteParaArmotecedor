# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteTemperatura',
            fields=[
                ('teste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Teste')),
                ('teste_temperatura_um', models.IntegerField()),
                ('teste_temperatura_dois', models.IntegerField()),
            ],
            bases=('app.teste',),
        ),
        migrations.CreateModel(
            name='TesteTempo',
            fields=[
                ('teste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Teste')),
                ('teste_tempo_inicio', models.TimeField(null=True)),
            ],
            bases=('app.teste',),
        ),
    ]
