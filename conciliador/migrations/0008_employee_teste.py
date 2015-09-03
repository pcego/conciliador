# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0007_auto_20150903_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='teste',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
