# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0011_auto_20151202_1901'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lastSeenProducts',
            field=models.ManyToManyField(to='flowers.Flower'),
        ),
    ]
