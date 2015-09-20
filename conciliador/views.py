from django.shortcuts import render
from conciliador.forms import Vendas
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
