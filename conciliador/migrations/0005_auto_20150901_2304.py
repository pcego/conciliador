# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0004_salepackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Bandeira',
            },
        ),
        migrations.CreateModel(
            name='ProductPurchaser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('service_tax', models.DecimalField(max_digits=10, decimal_places=2)),
                ('receipt_forecast', models.IntegerField()),
                ('bank', models.CharField(max_length=100)),
                ('agency', models.CharField(max_length=10)),
                ('account', models.CharField(max_length=100)),
                ('flag', models.ForeignKey(to='conciliador.Flag')),
            ],
            options={
                'verbose_name': 'Produto_Adquirente',
            },
        ),
        migrations.CreateModel(
            name='Purchaser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('contract', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('device_rent_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('antecipation_tax', models.DecimalField(max_digits=10, decimal_places=2)),
                ('validate', models.DateField(help_text='Formato: dd/MM/aaaa')),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(to='conciliador.Company')),
            ],
            options={
                'verbose_name': 'Adquirente',
            },
        ),
        migrations.RenameField(
            model_name='neighborhood',
            old_name='city_id',
            new_name='city',
        ),
        migrations.AddField(
            model_name='productpurchaser',
            name='purchaser',
            field=models.ForeignKey(to='conciliador.Purchaser'),
        ),
    ]
