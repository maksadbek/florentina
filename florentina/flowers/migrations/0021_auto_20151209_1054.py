# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0020_auto_20151209_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 10, 54, 6, 668346, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 10, 54, 6, 668388, tzinfo=utc)),
        ),
    ]
