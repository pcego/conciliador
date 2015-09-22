from django import forms

class Vendas(forms.Form):
    cliente_id = forms.CharField(
        label='Codigo do cliente', max_length=100)

class Recebimentos(forms.Form):
    cliente_id = forms.CharField(
        label='Codigo do cliente', max_length=100)
    status = forms.CharField(
        label='Status do retorno - TODOS, CONCILIADOS, PENDENTES e CONCILIADOS_MANUALMENTE - DEFAULT TODOS.', 
        max_length=100)
    dataInicial = forms.CharField(
        label='Data inicial', max_length=100)
    dataFinal = forms.CharField(
        label='Data final', max_length=100)
    adquirente = forms.CharField(
        label='Adquirente', max_length=100)
    bandeira = forms.CharField(
        label='Bandeira', max_length=100)
    tipoRetorno = forms.CharField(
        label='Tipo de retorno: LANCAMENTO ou CONCILIACAO(Default)', max_length=100)