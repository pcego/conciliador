# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0003_auto_20150828_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalePackage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sale_date', models.DateField(help_text='Ex: 29/07/2015')),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(to='conciliador.Company')),
                ('package', models.ForeignKey(to='conciliador.Package')),
            ],
            options={
                'verbose_name': 'VendadePacote',
            },
        ),
    ]
