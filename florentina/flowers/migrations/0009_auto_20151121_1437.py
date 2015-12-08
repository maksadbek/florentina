# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0008_auto_20151121_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 14, 37, 54, 872446, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 14, 37, 54, 872483, tzinfo=utc)),
        ),
    ]
