

class RetornoVendas(object):

    lista_retornos = []

    clienteId = 0
    filialId = 0
    adquirente = '',
    cnpj = ''
    bandeira = ''
    produto = ''
    numeroDaParcela = 0
    quantidadeDeParcelas = 0
    valorBruto = 0
    valorLiquido = 0
    cliente = ''
    dataVenda = Date
    origem = ''
    key = ''
    notaFiscal = ''

    def __init__(self):
        pass

    def parse(json):
        for retorno in json:
            self.adquirente = retorno['adquirente']
            self.bandeira = retornos['bandeira']
            self.data = retorno['data']
            self.lista_retornos.append(obj)