# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotteryuser',
            name='number',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
