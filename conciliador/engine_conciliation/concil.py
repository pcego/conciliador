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

        try:
            lista_vendas = json.loads(r.data.decode('utf-8'))['retornos']
            for v in  lista_vendas:
                venda.parse(v)
                lista_retornos.append(venda)
        except Exception:
            pass
            # Gravar no log 
        return lista_retornos

    def retorno_recebimentos(self, client_id, status, dataInicial, 
        dataFinal, adquirente, bandeira, tipoRetorno):

        lista_recebimentos = []

        r = self.http.request(
            'GET', self.url + settings.URL_RETORNO_RECEBIMENTOS,
            {'clienteId':client_id, 'status':status, 'dataInicial':dataInicial, 
            'dataFinal':dataFinal, 'adquirente':adquirente, 'bandeira':bandeira, 
            'tipoRetorno':tipoRetorno})

        lista_recebimentos = json.loads(r.data.decode('utf-8'))['retornos']

        return lista_recebimentos

    def conciliacoes_vendas(self, client_id):
        lista_conciliacoes_vendas = []
       
        r = self.http.request(
            'GET', self.url + settings.URL_CONCILIACOES_VENDAS,
            {'clienteId':client_id})

        lista_conciliacoes_vendas = json.loads(r.data.decode('utf-8'))['conciliacoes']

        return lista_conciliacoes_vendas

    def lancamentos_vendas(self, client_id, data_inicial, data_final):
        
        lista_lancamentos = []
               
        r = self.http.request(
            'GET', self.url + settings.URL_LANCAMENTOS_VENDAS,
            {'clienteId':client_id, 'dataInicial':data_inicial, 'dataFinal': data_final})
        
        lista_lancamentos = json.loads(r.data.decode('utf-8'))['lancamentos']
        import pdb;pdb.set_trace()       
        return lista_lancamentos


    def lancamentos_filiais(self, client_id, data_inicial, data_final):
        
        lista_lancamentos_filiais = []
               
        r = self.http.request(
            'GET', self.url + settings.URL_LANCAMENTOS_VENDAS_FILIAIS,
            {'clienteId':client_id, 'dataInicial':data_inicial, 'dataFinal': data_final})
        
        lista_lancamentos_filiais = json.loads(r.data.decode('utf-8'))['lancamentos']
       
        return lista_lancamentos_filiais


    def conciliacoes_recebimentos(self, client_id, dataInicial, dataFinal):
        lista_conciliacoes_recebimentos = []
       
        r = self.http.request(
            'GET', self.url + settings.URL_CONCILIACOES_RECEBIMENTOS,
            {'clienteId':client_id, 'dataInicial':dataInicial, 'dataFinal': dataFinal})

        lista_conciliacoes_recebimentos = json.loads(r.data.decode('utf-8'))['conciliacoes']

        return lista_conciliacoes_recebimentos


    def lancamento_previsoes(self, client_id, dataInicial, dataFinal):
        
        lista_previsoes = []
       
        r = self.http.request(
            'GET', self.url + settings.URL_LANCAMENTOS_PREVISOES,
            {'clienteId':client_id, 'dataInicial':dataInicial, 'dataFinal': dataFinal})

        lista_previsoes = json.loads(r.data.decode('utf-8'))['lancamentos']

        return lista_previsoes


    def conciliacoes_vendas_filiais(self, client_id, dataInicial, dataFinal):
        lista_conciliacoes_vendas_filiais = []
       
        r = self.http.request(
            'GET', self.url + settings.URL_CONCILIACOES_VENDAS_FILIAIS,
            {'clienteId':client_id, 'dataInicial':dataInicial, 'dataFinal': dataFinal})

        lista_conciliacoes_vendas_filiais = json.loads(r.data.decode('utf-8'))['conciliacoes']

        return lista_conciliacoes_vendas_filiais