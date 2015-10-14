# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0013_remove_company_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('clienteId', models.IntegerField()),
                ('filialId', models.IntegerField()),
                ('adquirente', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=150)),
                ('bandeira', models.CharField(max_length=150)),
                ('produto', models.CharField(max_length=150)),
                ('numeroDaParcela', models.IntegerField()),
                ('quantidadeDeParcelas', models.IntegerField()),
                ('NSU', models.IntegerField()),
                ('autorizacao', models.IntegerField()),
                ('TID', models.IntegerField()),
                ('valorBruto', models.FloatField()),
                ('valorLiquido', models.FloatField()),
                ('cliente', models.CharField(max_length=150)),
                ('dataVenda', models.DateField()),
                ('origem', models.CharField(max_length=150)),
                ('key', models.CharField(max_length=150)),
                ('dataPrevisaoVencimento', models.DateField()),
                ('notaFiscal', models.CharField(max_length=150)),
            ],
        ),
    ]
