# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliveip',
            name='local',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='归属地'),
        ),
    ]
