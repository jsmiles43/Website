# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectCard', '0006_auto_20170401_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(),
        ),
    ]
