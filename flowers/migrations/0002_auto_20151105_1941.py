# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 5, 19, 41, 43, 689875, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 5, 19, 41, 43, 689953, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='flower',
            name='img',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='flower',
            name='category',
            field=models.ForeignKey(to='flowers.Category', null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='type',
            field=models.ForeignKey(to='flowers.Type', null=True),
        ),
    ]
