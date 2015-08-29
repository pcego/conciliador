# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conciliador', '0002_auto_20150827_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company_name', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=30)),
                ('state_registration', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=20)),
                ('fantasy_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('complement', models.CharField(max_length=100)),
                ('concil_id_branch', models.CharField(max_length=100)),
                ('concil_id_customer', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('boss', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('neighborhood', models.ForeignKey(to='conciliador.Neighborhood')),
                ('parent_company', models.ForeignKey(help_text='Empresa Matriz', related_name='branch_parent_company', null=True, blank=True, to='conciliador.Company')),
            ],
            options={
                'verbose_name': 'Empresa',
            },
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name': 'Pacote'},
        ),
    ]
