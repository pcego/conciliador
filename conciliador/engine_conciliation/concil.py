from project import settings
import urllib3, json
from conciliador.engine_conciliation.models.venda import Venda


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