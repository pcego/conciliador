class ConciliacoesVendas(object):

    def __init__(slef):
        quantidadeLancamentosConta = 0
        quantidadeLancamentosContrapartida = 0
        valorConta = 0.0
        valorContraPartida = 0.0
        diferenca = 0.0
        bandeira = ''
        adquirente = ''
        links = []

    def parse(self, conciliacoesVendas):
        self.clienteId = int(conciliacoesVendas['clienteId'])
        self.quantidadeLancamentosConta = int(conciliacoesVendas['quantidadeLancamentosConta'])
        self.quantidadeLancamentosContrapartida = int(conciliacoesVendas['quantidadeLancamentosContrapartida'])
        self.valorConta = float(conciliacoesVendas['valorConta'])
        self.valorContraPartida = float(conciliacoesVendas['valorContraPartida'])
        self.diferenca =  float(conciliacoesVendas['diferenca'])
        self.bandeira = conciliacoesVendas['bandeira']
        self.adquirente = conciliacoesVendas['adquirente']
 #     self.links = []        
 #     for item in conciliacoesVendas['links']:
 #     links.append(item)