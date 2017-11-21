# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0004_auto_20171120_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotoBranco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branco', models.CharField(choices=[('True', 'Branco')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='voto',
            name='branco',
        ),
        migrations.AddField(
            model_name='eleitor',
            name='token',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='eleitor',
            name='votou',
            field=models.NullBooleanField(verbose_name='VOTOU: '),
        ),
    ]