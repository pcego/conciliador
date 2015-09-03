# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0010_auto_20150903_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productpurchaser',
            options={'verbose_name': 'Produto Adquirente'},
        ),
        migrations.AddField(
            model_name='flag',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productpurchaser',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
