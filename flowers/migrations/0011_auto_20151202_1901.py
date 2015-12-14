# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0010_auto_20151202_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 19, 1, 39, 148321, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 19, 1, 39, 148358, tzinfo=utc)),
        ),
    ]
