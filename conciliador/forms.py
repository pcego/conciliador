from django import forms
from conciliador.models import Venda
from django.forms import ModelForm

class Vendas(forms.Form):
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=100)
    statusConciliacao =  forms.CharField(label='Status do retorno - TODOS, CONCILIADOS, PENDENTES E CONCILIADOS_MANUALMENTE', max_length=100)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)

class RetornosRecebimentos(forms.Form):
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=100)
    status = forms.CharField(label='Status do retorno', max_length=100)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)
    adquirente = forms.CharField(label='Adquirente', max_length=100)
    bandeira = forms.CharField(label='Bandeira', max_length=100)
    tipoRetorno = forms.CharField(label='Tipo de retorno', max_length=100)


class ConciliacoesVendas(forms.Form):
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=100)
    data_Inicial = forms.CharField(label='Data Inicial', max_length=20)
    data_Final = forms.CharField(label='Data Final', max_length=20)


class Lancamento(forms.Form):
    cliente_id = forms.CharField(label='Código do Cliente', max_length = 100)
    data_inicial = forms.CharField(label='Data Inicial', max_length=20)
    data_final = forms.CharField(label='Data Final', max_length=20)


class LancamentoFilial(forms.Form):
    cliente_id = forms.CharField(label='Código do Cliente', max_length = 100)
    data_inicial = forms.CharField(label='Data Inicial', max_length=20)
    data_final = forms.CharField(label='Data Final', max_length=20)
     

class ConciliacoesRecebimentos(forms.Form):
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=100)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)


class LancamentoPrevisao(forms.Form):
    cliente_id = forms.CharField(label='Código do Cliente', max_length = 100)
    data_inicial = forms.CharField(label='Data Inicial', max_length=20)
    data_final = forms.CharField(label='Data Final', max_length=20)


class ConciliacoesVendasFiliais(forms.Form):
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=100)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)

class FormVenda(ModelForm):
    class Meta:
        model = Venda
        exclude = ['']

class ConciliacoesRecebimentosFiliais(forms.Form):
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=20)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)

class ConciliacoesRecebimentosFiliaisId(forms.Form):
    id_filial = forms.CharField(label='Id da filial', max_length=20)
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=20)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)

class ConciliacoesVendasFiliaisId(forms.Form):
    id_filial = forms.CharField(label='Id da filial', max_length=20)
    cliente_id = forms.CharField(label='Codigo do cliente', max_length=100)
    dataInicial = forms.CharField(label='Data inicial', max_length=100)
    dataFinal = forms.CharField(label='Data final', max_length=100)