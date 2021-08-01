# import config
#CMCapi_key=config.CMCapi_key
import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC,ETH,XRP,MATIC,MATICBULL,CRO,VET',
  'aux':'volume_7d_reported'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.CMC_api,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  rawdata = json.loads(response.text)
  #print(data)
  CoinPrice={}
  CoinPriceChange1h={}
  CoinPriceChange24h={}
  rawdata=rawdata['data']
  for coin in ['BTC','CRO','ETH','MATIC','MATICBULL','VET','XRP']:
    CoinPrice[coin]=rawdata[coin]['quote']['USD']['price']
    CoinPriceChange1h[coin]=rawdata[coin]['quote']['USD']['percent_change_1h']
    CoinPriceChange24h[coin]=rawdata[coin]['quote']['USD']['percent_change_24h']
    print('%10s'%coin,"price is",'{: 9.2f}'.format(CoinPrice[coin]),"%.2f"%CoinPriceChange1h[coin],"%.2f"%CoinPriceChange24h[coin])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
