# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0009_auto_20150903_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 3, 23, 30, 45, 826928, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ManyToManyField(to='conciliador.Company'),
        ),
    ]
