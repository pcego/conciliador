# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciliador', '0015_conciliacoesrecebimentos_conciliacoesrecebimentosfiliais_conciliacoesrecebimentosfiliaisid_conciliac'),
    ]

    operations = [
        migrations.CreateModel(
            name='LancamentoRecebimento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('adquirente', models.CharField(max_length=150)),
                ('bandeira', models.CharField(max_length=150)),
                ('quant_lanc_conta', models.IntegerField()),
                ('quant_lançamentos_contra', models.IntegerField()),
                ('valor_total_conta', models.FloatField()),
                ('valor_contra_partida', models.FloatField()),
                ('dif_conc', models.FloatField()),
            ],
        ),
    ]
