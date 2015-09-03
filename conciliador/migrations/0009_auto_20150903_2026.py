# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0008_employee_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='teste',
        ),
        migrations.AddField(
            model_name='employee',
            name='complement',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='cpf',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='neighborhood',
            field=models.ForeignKey(default=1, to='conciliador.Neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='street',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
