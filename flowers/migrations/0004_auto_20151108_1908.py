# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0003_auto_20151105_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='popularity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 19, 8, 21, 664583, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 19, 8, 21, 664646, tzinfo=utc)),
        ),
    ]
