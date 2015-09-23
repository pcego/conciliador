from project import settings
import urllib3, json
from conciliador.engine_conciliation.models.venda import Venda
from conciliador.engine_conciliation.models.recebimentos import Recebimentos
from conciliador.engine_conciliation.models.conciliacoesvendas import ConciliacoesVendas
class Concil(object):

    def __init__(self):
        self.http = urllib3.PoolManager()
        self.url = settings.URL_MAIN
        self.http.headers['app-token'] = settings.APP_TOKEN

    def retorno_vendas(self, client_id):
        lista_retornos = []
        lista_vendas = []
        venda = Venda()

        r = self.http.request(
            'GET', self.url + settings.URL_RETORNO_VENDAS,
            {'clienteId':client_id})

        lista_vendas = json.loads(r.data.decode('utf-8'))['retornos']

        for v in  lista_vendas:
            venda.parse(v)
            lista_retornos.append(venda)

        return lista_retornos

    def retorno_recebimentos(self, client_id, status, dataInicial, dataFinal, adquirente, bandeira, tipoRetorno):
        lista_retornos = []
        lista_recebimentos = []
        recebimentos = Recebimentos()

        r = self.http.request(
            'GET', self.url + settings.URL_RETORNO_RECEBIMENTOS,
            {'clienteId':client_id, 'status':status, 'dataInicial':dataInicial, 'dataFinal':dataFinal, 'adquirente':adquirente, 'bandeira':bandeira, 'tipoRetorno':tipoRetorno})

        lista_recebimentos = json.loads(r.data.decode('utf-8'))['retornos']

        for v in  lista_recebimentos:
            recebimentos.parse(v)
            lista_retornos.append(recebimentos)

        return lista_retornos

    def conciliacoes_vendas(self, client_id):
        lista_retornos = []
        lista_conciliacoes_vendas = []
        conciliacoesvendas = ConciliacoesVendas()

        r = self.http.request(
            'GET', self.url + settings.URL_RETORNO_RECEBIMENTOS,
            {'clienteId':client_id})

        conciliacoes_vendas = json.loads(r.data.decode('utf-8'))['conciliacoes']

        for v in  conciliacoes_vendas:
            conciliacoesvendas.parse(v)
            lista_retornos.append(conciliacoesvendas)

        return lista_retornos