# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 12, 14, 22, 25, 38, 151815, tzinfo=utc))),
                ('img', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 12, 14, 22, 25, 38, 152815, tzinfo=utc), editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime(2015, 12, 14, 22, 25, 38, 152815, tzinfo=utc))),
                ('popularity', models.IntegerField()),
            ],
        ),
    ]
