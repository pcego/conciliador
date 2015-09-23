from django.shortcuts import render
from conciliador.forms import Vendas, Recebimentos, ConciliacoesVendas
from conciliador.forms import Lancamento
from conciliador.engine_conciliation.concil import Concil

def home(request):
    return render(request, 'conciliador/index.html')

def vendas(request):
    data = {}

    if request.method == 'POST':
        form = Vendas(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.retorno_vendas(client_id=form.cleaned_data['cliente_id'])
            form = Vendas()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = Vendas()
        data['form'] = form
    return render(request, 'conciliador/vendas.html', data)

def recebimentos(request):
    data = {}

    if request.method == 'POST':
        form = Recebimentos(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.retorno_recebimentos(client_id=form.cleaned_data['cliente_id'], status=form.cleaned_data['status'], 
                dataInicial=form.cleaned_data['dataInicial'], dataFinal=form.cleaned_data['dataFinal'], 
                adquirente=form.cleaned_data['adquirente'], bandeira=form.cleaned_data['bandeira'], 
                tipoRetorno=form.cleaned_data['tipoRetorno'])
            form = Recebimentos()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = Recebimentos()
        data['form'] = form
    return render(request, 'conciliador/recebimentos.html', data)

def conciliacoes_vendas(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesVendas(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.conciliacoes_vendas(client_id=form.cleaned_data['cliente_id'])
            form = ConciliacoesVendas()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = ConciliacoesVendas()
        data['form'] = form
    return render(request, 'conciliador/conciliacoes_vendas.html', data)

def lancamentos_vendas(request):

    data = {}

    if request.method == 'POST':
        form = Lancamento(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.lancamentos_vendas(
                client_id=form.cleaned_data['cliente_id'], 
                data_Inicial=form.cleaned_data['data_Inicial'], 
                data_Final=form.cleaned_data['data_Final'],)
            form = Lancamento()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = Lancamento()
        data['form'] = form
    return render(request, 'conciliador/lancamentos_vendas.html', data)
