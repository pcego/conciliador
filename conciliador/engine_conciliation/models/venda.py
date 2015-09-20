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


'''{'filialCodigo': '001', 'tid': '0', 'nsu': '123456789012345', 'valorLiquidoConta': '250.00', 'produto': 'CREDITO', 'key': '12560', 'filialId': 8, 'statusConciliacao': 'PENDENTE', 'sistemaOrigem': 'PRESENCE', 'adquirente': 'CIELO', 'bandeira': 'AMEX', 'notaFiscal': '1448305', 'dataDePrevisaoDoVencimento': '30/09/2015', 'quantidadeDeParcelas': 0, 'lancamentoId': 748401, 'clienteId': '1', 'valorBrutoConta': '260.00', 'numeroDaParcela': 1, 'dataVenda': '16/09/2015', 'autorizacao': '0'}'''
