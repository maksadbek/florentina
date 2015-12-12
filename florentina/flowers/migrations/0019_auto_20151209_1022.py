# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0018_auto_20151204_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 10, 22, 8, 971317, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 10, 22, 8, 971447, tzinfo=utc)),
        ),
    ]