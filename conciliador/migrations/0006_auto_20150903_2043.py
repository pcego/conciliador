# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0005_auto_20150901_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('talk_with', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(to='conciliador.Company')),
            ],
            options={
                'verbose_name': 'Contato',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo Contato',
            },
        ),
        migrations.CreateModel(
            name='TypeContact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type_contact', models.CharField(max_length=100)),
                ('masks', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Departamento',
            },
        ),
        migrations.AlterModelOptions(
            name='productpurchaser',
            options={'verbose_name': 'Produto Adquirente'},
        ),
        migrations.AddField(
            model_name='contact',
            name='department',
            field=models.ForeignKey(to='conciliador.Department'),
        ),
        migrations.AddField(
            model_name='contact',
            name='type_contact',
            field=models.ForeignKey(to='conciliador.TypeContact'),
        ),
    ]
