# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 06:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0022_auto_20151209_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 6, 47, 18, 743530, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 6, 47, 18, 743573, tzinfo=utc)),
        ),
    ]
