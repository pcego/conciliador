# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0014_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConciliacoesRecebimentos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantidadeLancamentosConta', models.IntegerField()),
                ('quantidadeLancamentosContrapartida', models.IntegerField()),
                ('valorConta', models.FloatField()),
                ('valorContraPartida', models.FloatField()),
                ('diferenca', models.FloatField()),
                ('bandeira', models.CharField(max_length=150)),
                ('adquirente', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ConciliacoesRecebimentosFiliais',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantidadeLancamentosConta', models.IntegerField()),
                ('quantidadeLancamentosContrapartida', models.IntegerField()),
                ('valorConta', models.FloatField()),
                ('valorContraPartida', models.FloatField()),
                ('diferenca', models.FloatField()),
                ('bandeira', models.CharField(max_length=150)),
                ('adquirente', models.CharField(max_length=150)),
                ('nomeFilial', models.CharField(max_length=150)),
                ('filialCodigo', models.CharField(max_length=150)),
                ('filialId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConciliacoesRecebimentosFiliaisID',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantidadeLancamentosConta', models.IntegerField()),
                ('quantidadeLancamentosContrapartida', models.IntegerField()),
                ('valorConta', models.FloatField()),
                ('valorContraPartida', models.FloatField()),
                ('diferenca', models.FloatField()),
                ('bandeira', models.CharField(max_length=150)),
                ('adquirente', models.CharField(max_length=150)),
                ('nomeFilial', models.CharField(max_length=150)),
                ('filialCodigo', models.CharField(max_length=150)),
                ('filialId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConciliacoesVendas',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantidadeLancamentosConta', models.IntegerField()),
                ('quantidadeLancamentosContrapartida', models.IntegerField()),
                ('valorConta', models.FloatField()),
                ('valorContraPartida', models.FloatField()),
                ('diferenca', models.FloatField()),
                ('bandeira', models.CharField(max_length=150)),
                ('adquirente', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ConciliacoesVendasFiliais',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantidadeLancamentosConta', models.IntegerField()),
                ('quantidadeLancamentosContrapartida', models.IntegerField()),
                ('valorConta', models.FloatField()),
                ('valorContraPartida', models.FloatField()),
                ('diferenca', models.FloatField()),
                ('bandeira', models.CharField(max_length=150)),
                ('adquirente', models.CharField(max_length=150)),
                ('nomeFilial', models.CharField(max_length=150)),
                ('filialCodigo', models.CharField(max_length=150)),
                ('filialId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConciliacoesVendasFiliaisID',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantidadeLancamentosConta', models.IntegerField()),
                ('quantidadeLancamentosContrapartida', models.IntegerField()),
                ('valorConta', models.FloatField()),
                ('valorContraPartida', models.FloatField()),
                ('diferenca', models.FloatField()),
                ('bandeira', models.CharField(max_length=150)),
                ('adquirente', models.CharField(max_length=150)),
                ('nomeFilial', models.CharField(max_length=150)),
                ('filialCodigo', models.CharField(max_length=150)),
                ('filialId', models.IntegerField()),
            ],
        ),
    ]
