# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='popularity',
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 12, 14, 22, 35, 43, 41159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 22, 35, 43, 41159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 22, 35, 43, 41159, tzinfo=utc)),
        ),
    ]
