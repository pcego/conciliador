from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'conciliador.views.home', name='conc_home'),
    url(r'^retornos/vendas/', 'conciliador.views.retornos_vendas',name='url_retornos_vendas'),
    url(r'^retornos/recebimentos/', 'conciliador.views.retornos_recebimentos',name='url_retornos_recebimentos'),
    url(r'^lancamentos/vendas$', 'conciliador.views.lancamentos_vendas',name='url_lancamentos'),
    url(r'^lancamentos/vendas/filiais', 'conciliador.views.lancamentos_filiais',name='url_lancamentos_filiais'),
    url(r'^conciliacoes/recebimentos', 'conciliador.views.conciliacoes_recebimentos',name='url_conciliacoes_recebimentos'),  
    url(r'^conciliacoes/vendas$', 'conciliador.views.conciliacoes_vendas',name='url_conciliacoes_vendas'),
    url(r'^conciliacoes/vendas/filiais', 'conciliador.views.conciliacoes_vendas_filiais',name='url_conciliacoes_vendas_filiais'),  
]
