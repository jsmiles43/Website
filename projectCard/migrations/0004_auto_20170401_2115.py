# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectCard', '0003_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='url',
            field=models.URLField(max_length=50, null=True),
        ),
    ]