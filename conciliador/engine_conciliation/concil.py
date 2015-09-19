from project import settings
import urllib3, json
from models import RetornoVendas, Venda


class Concil(object):

    def __init__(self):
        self.http = urllib3.PoolManager()
        self.url = settings.URL_MAIN
        self.http.headers['app-token'] = settings.APP_TOKEN

    def retorno_vendas(self, client_id):
        lista_retornos = []
        venda = Venda()

        r = self.http.request('GET', self.url + settings.URL_RETORNO_VENDAS, {'clienteId':client_id})

        for retorno in  json.loads(r.data.decode('utf-8')
            venda.parse(retorno)
            lista_retornos.append(venda)

        return lista_retornos
