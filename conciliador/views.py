from django.shortcuts import render
from conciliador.forms import Vendas, RetornosRecebimentos
from conciliador.forms import ConciliacoesVendasFiliais
from conciliador.forms import Lancamento, LancamentoFilial
from conciliador.forms import ConciliacoesRecebimentos, FormVenda
from conciliador.forms import ConciliacoesVendas
from conciliador.forms import LancamentoPrevisao
from conciliador.forms import ConciliacoesRecebimentosFiliais
from conciliador.forms import ConciliacoesRecebimentosFiliaisId
from conciliador.forms import ConciliacoesVendasFiliaisId
from conciliador.forms import LancamentoRecebimento
from conciliador.forms import LancamentoRecebimentoFilial
from conciliador.forms import LancamentoPrevisaoFilial
from conciliador.engine_conciliation.concil import Concil

def home(request):
    return render(request, 'conciliador/index.html')

def retornos_vendas(request):
    data = {}

    if request.method == 'POST':
        form = Vendas(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.retorno_vendas(
                client_id=form.cleaned_data['cliente_id'],
                statusConciliacao=form.cleaned_data['statusConciliacao'],
                dataInicial=form.cleaned_data['dataInicial'], 
                dataFinal=form.cleaned_data['dataFinal'])    
            form = Vendas()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = Vendas()
        data['form'] = form
    return render(request, 'conciliador/vendas.html', data)

def retornos_recebimentos(request):
    data = {}

    if request.method == 'POST':
        form = RetornosRecebimentos(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.retorno_recebimentos(client_id=form.cleaned_data['cliente_id'], 
                status=form.cleaned_data['status'], 
                dataInicial=form.cleaned_data['dataInicial'], dataFinal=form.cleaned_data['dataFinal'], 
                adquirente=form.cleaned_data['adquirente'], bandeira=form.cleaned_data['bandeira'], 
                tipoRetorno=form.cleaned_data['tipoRetorno'])
            form = RetornosRecebimentos()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = RetornosRecebimentos()
        data['form'] = form
    return render(request, 'conciliador/retornos_recebimentos.html', data)

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

def conciliacoes_vendas_filiais(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesVendasFiliais(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.conciliacoes_vendas_filiais(
                client_id=form.cleaned_data['cliente_id'], 
                dataInicial=form.cleaned_data['dataInicial'], 
                dataFinal=form.cleaned_data['dataFinal'])    
            form = ConciliacoesVendasFiliais()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = ConciliacoesVendasFiliais()
        data['form'] = form
    return render(request, 'conciliador/conciliacoes_vendas_filiais.html', data)


def venda(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesVendasFiliais(request.POST or None)

        if form.is_valid():
            form.save()
            conc = Concil()        
            lista = conc.nova_venda(vendasRequest=form.cleaned_data['vendasRequest'])
            data=['Venda salva com sucesso']
            form = FormVenda()
            data['form'] = form
        else:
            data['form'] = form
    else:
        form = FormVenda()
        data['form'] = form

    return render(request, 'conciliador/nova_vendas.html', data)

def conciliacoes_recebimentos_filiais(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesRecebimentosFiliais(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.conciliacoes_recebimentos_filiais(
                client_id=form.cleaned_data['cliente_id'], 
                dataInicial=form.cleaned_data['dataInicial'], 
                dataFinal=form.cleaned_data['dataFinal'])
            form = ConciliacoesRecebimentosFiliais()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = ConciliacoesRecebimentosFiliais()
        data['form'] = form
    return render(request, 'conciliador/conciliacoes_recebimentos_filiais.html', data)

def conciliacoes_recebimentos_filiais_id(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesRecebimentosFiliaisId(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.conciliacoes_recebimentos_filiais_id(
                id_filial = form.cleaned_data['id_filial'], 
                client_id=form.cleaned_data['cliente_id'], 
                dataInicial=form.cleaned_data['dataInicial'],
                dataFinal=form.cleaned_data['dataFinal'])
            form = ConciliacoesRecebimentosFiliaisId()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = ConciliacoesRecebimentosFiliaisId()
        data['form'] = form
    return render(request, 'conciliador/conciliacoes_recebimentos_filiais_id.html', data)

def conciliacoes_vendas_filiais_id(request):
    data = {}

    if request.method == 'POST':
        form = ConciliacoesVendasFiliaisId(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.conciliacoes_vendas_filiais_id(
                id_filial = form.cleaned_data['id_filial'], 
                client_id=form.cleaned_data['cliente_id'], 
                dataInicial=form.cleaned_data['dataInicial'], 
                dataFinal=form.cleaned_data['dataFinal'])    
            form = ConciliacoesVendasFiliaisId()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = ConciliacoesVendasFiliaisId()
        data['form'] = form
    return render(request, 'conciliador/conciliacoes_vendas_filiais_id.html', data)


def lancamentos_recebimentos(request):
    
    data = {}

    if request.method == 'POST':
        form = LancamentoRecebimento(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.lancamento_recebimentos(
                client_id=form.cleaned_data['cliente_id'], 
                data_inicial=form.cleaned_data['data_inicial'], 
                data_final=form.cleaned_data['data_final'],    
                limite=form.cleaned_data['limite'])  

            form = LancamentoRecebimento()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = LancamentoRecebimento()
        data['form'] = form
    return render(request, 'conciliador/lancamentos_recebimentos.html', data)



def lancamentos_recebimentos_filiais(request):
    
    data = {}

    if request.method == 'POST':
        form = LancamentoRecebimentoFilial(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.lancamentos_recebimentos_filiais(
                client_id=form.cleaned_data['cliente_id'], 
                data_inicial=form.cleaned_data['data_inicial'], 
                data_final=form.cleaned_data['data_final'])  

            form = LancamentoRecebimentoFilial()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = LancamentoRecebimentoFilial()
        data['form'] = form
    return render(request, 'conciliador/lancamentos_receb_filiais.html', data)



def lancamentos_previsoes_filiais(request):
    
    data = {}





































































































































































































































































































































    

    if request.method == 'POST':
        form = LancamentoPrevisaoFilial(request.POST or None)

        if form.is_valid():
            conc = Concil()        
            lista = conc.lancamentos_previsoes_filiais(
                client_id=form.cleaned_data['cliente_id'], 
                data_inicial=form.cleaned_data['data_inicial'], 
                data_final=form.cleaned_data['data_final'])  

            form = LancamentoPrevisaoFilial()
            data['form'] = form
            data['lista'] = lista
        else:
            data['form'] = form
    else:
        form = LancamentoPrevisaoFilial()
        data['form'] = form
    return render(request, 'conciliador/lancamentos_previsoes_filiais.html', data)