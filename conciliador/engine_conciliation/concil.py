from project import settings
import urllib3, json


class Concil(object):

    def __init__(self):
        self.http = urllib3.PoolManager()
        self.url = settings.URL_MAIN
        self.http.headers['app-token'] = settings.APP_TOKEN

    def retorno_vendas(self, client_id):
        r = self.http.request('GET', self.url + settings.URL_RETORNO_VENDAS, {'clienteId':client_id})
        
        for retornos in json.loads(r.data.decode('utf-8')):
            for ret in retornos:
                print (retornos['adquirente'], retornos['autorizacao'], retornos['bandeira'])


        #Agora e fazer o parse e devolver um objeto