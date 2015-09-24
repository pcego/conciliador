from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'conciliador.views.home', name='conc_home'),
    url(r'^vendas/', 'conciliador.views.vendas',name='url_vendas'),
    url(r'^recebimentos/', 'conciliador.views.recebimentos',name='url_recebimentos'),
    url(r'^conciliacoes/vendas', 'conciliador.views.conciliacoes_vendas',name='url_conciliacoesvendas'),
    url(r'^lancamentos/vendas$', 'conciliador.views.lancamentos_vendas',name='url_lancamentos'),
    url(r'^lancamentos/vendas/filiais', 'conciliador.views.lancamentos_filiais',name='url_lancamentos_filiais'),
    url(r'^conciliacoes/recebimentos', 'conciliador.views.conciliacoes_recebimentos',name='url_conciliacoesrecebimentos'),  
]
