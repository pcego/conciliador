from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'conciliador.views.home', name='conc_home'),
    url(r'^vendas/', 'conciliador.views.vendas',name='url_vendas'),
    url(r'^recebimentos/', 'conciliador.views.recebimentos',name='url_recebimentos'),
    url(r'^conciliacoesvendas/', 'conciliador.views.conciliacoesvendas',name='url_conciliacoesvendas'),
]
