# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('data', models.DateField(verbose_name='Data')),
                ('vencedor', models.CharField(max_length=128)),
                ('candidatos', models.ManyToManyField(related_name='CandidatosEleicao', to='eleicao.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='VotoBranco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.CharField(max_length=7, verbose_name='branco')),
            ],
        ),
    ]