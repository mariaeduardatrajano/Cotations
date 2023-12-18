import requests

def get_cotacao():
  request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL').json()
  cotacao_dolar = request['USDBRL']['bid']
  cotacao_euro = request['EURBRL']['bid']
  cotacao_btc =  request['BTCBRL']['bid']

  return {'$' : cotacao_dolar, '€' : cotacao_euro, 'BTC' : cotacao_btc}

print(get_cotacao())