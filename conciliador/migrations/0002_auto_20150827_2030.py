# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cidade',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('city_id', models.ForeignKey(to='conciliador.City')),
            ],
            options={
                'verbose_name': 'Bairro',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=2)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Estado',
            },
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name': 'Pacotes'},
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='conciliador.State'),
        ),
    ]
