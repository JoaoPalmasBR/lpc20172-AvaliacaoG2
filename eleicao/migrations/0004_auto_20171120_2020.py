# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0003_auto_20171120_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Candidato'),
        ),
    ]
