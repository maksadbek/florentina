# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_auto_20151105_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 5, 20, 53, 19, 552556, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='img',
            field=models.ImageField(upload_to=b'images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 5, 20, 53, 19, 552629, tzinfo=utc)),
        ),
    ]
