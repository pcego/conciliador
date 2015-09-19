#coding:utf-8
import urllib3, json

http = urllib3.PoolManager()
http.headers['app-token'] = 'LICin04WKos8'
http.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
r = http.request('GET', 'http://sandbox.concildesenvolvedores.com.br/concilcard/v1/retornos/vendas',  {'clienteId': 1})
r = http.request('GET', 'http://sandbox.concildesenvolvedores.com.br/concilcard/v1/retornos/vendas?clienteId=1')
                                      'http://sandbox.concildesenvolvedores.com.br/concilcard/v1/retornos/vendas?clienteId=1'

# Exemple
http = urllib3.PoolManager()
r = http.request('GET', 'http://worldcup.sfg.io/matches ')
r = http.request('GET', 'http://sandbox.concildesenvolvedores.com.br:80/concilcard/v1/retornos/vendas',  {'clienteId': 1})

for jogo in json.loads(r.data.decode('utf-8')):
    if jogo['status'] == 'completed':
        print (jogo['match_number'], jogo['home_team']['country'],
            jogo['home_team']['goals'], 'x', jogo['away_team']['country'], jogo['away_team']['goals'], ' - Vencedor: ', jogo['winner'] )

TOKEN_BAIANO = 'LICin04WKos8' #Indicado pela concil
MY_TOKEN =        'ojukA6UdQMQ0'
HOST = 'sandbox.concildesenvolvedores.com.br'

'''vendasRequest {
    clienteId: 1, #id do cliente,
    filialId: 1, #id da filial do lado Concil,
    adquirente: 'CIELO', #Adquirente - Ver opcoes no link - http://concildesenvolvedores.com.br/api-portal/node/1126,
    cnpj: '08911905000125', #CNPJ da loja filial,
    bandeira: 'VISA', #Bandeira - Ver opcoes no link - http://concildesenvolvedores.com.br/api-portal/node/1126,
    produto: 'DEBITO', #produto - Ver opções no link - http://concildesenvolvedores.com.br/api-portal/node/1126,
    numeroDaParcela: 1, # (int, optional): Número da parcela da transação,
    quantidadeDeParcelas: 12,# (int): Quantidade de parcelas,
    #NSU:  (int, optional): Sequencial único que identifica a transação na Adquirente (Quando menor que 15 dígitos completar com zeros a esquerda).,
    #autorizacao (int, optional): Número de autorização da Bandeira na transação,
    #TID (int, optional): Identificador da transação em E-Commerce,
    valorBruto: 400, # (double): Valor da parcela da venda,
    valorLiquido: 300, # (double, optional): Valor líquido da parcela(Descontado a taxa de administração),
    cliente: 'Gregory Pacheco', # (string, optional): Nome do cliente,
    dataVenda: 01012015, (date): Data da venda no formato DDMMYYYY,
    origem: 'TEF', # (string): Parceiro/ TEF/ ERP,
    key: '4543234', #(string): Chave de identificação do lançamento,
    #dataPrevisaoVencimento (data, optional): Data de previsão de vencimento da parcela,
    notaFiscal: '54354', # (string, optional): Número da nota fiscal de venda
}

vendasRequest {
    clienteId: 1, 
    filialId: 1, 
    adquirente: 'CIELO',
    cnpj: '08911905000125',
    bandeira: 'VISA', 
    produto: 'DEBITO',
    numeroDaParcela: 1,
    quantidadeDeParcelas: 12,
    valorBruto: 400,
    valorLiquido: 300,
    cliente: 'Gregory Pacheco',
    dataVenda: 01012015,
    origem: 'TEF',
    key: '4543234',
    notaFiscal: '54354',
}'''