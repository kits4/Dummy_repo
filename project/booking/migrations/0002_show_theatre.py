# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='theatre',
            field=models.CharField(blank=True, default='Waves Cinema', max_length=30, null=True),
        ),
    ]
