# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectCard', '0004_auto_20170401_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='url',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]