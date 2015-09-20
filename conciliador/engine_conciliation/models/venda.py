class Venda(object):
    
    def __init__(slef):
        clienteId = 0
        filialId = 0
        adquirente = '',
        cnpj = ''
        bandeira = ''
        statusConciliacao = ''
        produto = ''
        numeroDaParcela = 0
        quantidadeDeParcelas = 0
        valorBrutoConta = 0
        valorLiquidoConta = 0
        lancamentoId = ''
        cliente = ''
        dataVenda = ''
        sistemaOrigem = ''
        origem = ''
        key = ''
        notaFiscal = ''

    def parse(self, venda):
        self.clienteId = int(venda['clienteId'])
        self.filialId = int(venda['filialId'])
        self.adquirente = venda['adquirente']
        self.bandeira = venda['bandeira']
        self.statusConciliacao = venda['statusConciliacao']
        self.produto = venda['produto']
        self.lancamentoId = venda['lancamentoId']
        self.numeroDaParcela = int(venda['numeroDaParcela'])
        self.quantidadeDeParcelas = int(venda['quantidadeDeParcelas'])
        self.valorBrutoConta = float(venda['valorBrutoConta'])
        self.valorLiquidoConta = float(venda['valorLiquidoConta'])
        self.dataVenda = venda['dataVenda']
        self.key = venda['key']
        self.notaFiscal = venda['notaFiscal']