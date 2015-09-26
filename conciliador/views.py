from django.shortcuts import render
from conciliador.forms import Vendas, Recebimentos
from conciliador.forms import Lancamento, LancamentoFilial
from conciliador.forms import Vendas, Recebimentos
from conciliador.forms import ConciliacoesVendas, ConciliacoesRecebimentos
from conciliador.forms import LancamentoPrevisao
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
            lista = conc.retorno_recebimentos(client_id=form.cleaned_data['cliente_id'], 
                status=form.cleaned_data['status'], 
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
                data_inicial=form.cleaned_data['data_inicial'], 
                data_final=form.cleaned_data['data_final'],)
            form = Lancamento()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = Lancamento()
        data['form'] = form
    return render(request, 'conciliador/lancamentos_vendas.html', data)


def lancamentos_filiais(request):
    
    data = {}

    if request.method == 'POST':
        form = LancamentoFilial(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.lancamentos_filiais(
                client_id=form.cleaned_data['cliente_id'], 
                data_inicial=form.cleaned_data['data_inicial'], 
                data_final=form.cleaned_data['data_final'],)
            form = LancamentoFilial()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = LancamentoFilial()
        data['form'] = form
        #import pdb;pdb.set_trace()
    return render(request, 'conciliador/lancamentos_filiais.html', data)


def conciliacoes_recebimentos(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesRecebimentos(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.conciliacoes_recebimentos(client_id=form.cleaned_data['cliente_id'], 
                dataInicial=form.cleaned_data['dataInicial'], dataFinal=form.cleaned_data['dataFinal'])    
            form = ConciliacoesRecebimentos()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = ConciliacoesRecebimentos()
        data['form'] = form
    return render(request, 'conciliador/conciliacoes_recebimentos.html', data)


def lancamentos_previsoes(request):
    
    data = {}

    if request.method == 'POST':
        form = LancamentoPrevisao(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.lancamento_previsoes(
                client_id=form.cleaned_data['cliente_id'], 
                data_inicial=form.cleaned_data['data_inicial'], 
                data_final=form.cleaned_data['data_final'])    
            form = LancamentoPrevisao()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = LancamentoPrevisao
        data['form'] = form
    return render(request, 'conciliador/lancamentos_previsoes.html', data)