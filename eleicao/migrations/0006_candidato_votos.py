# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0005_auto_20171120_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='votos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
