# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_auto_20160401_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bondactor',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='character',
            name='movies',
        ),
        migrations.AddField(
            model_name='gadget',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_app.Character'),
        ),
        migrations.AddField(
            model_name='movie',
            name='bond_actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_app.BondActor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(blank=True, to='api_app.Character'),
        ),
    ]
