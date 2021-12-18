##
## getquote-noxlsx 
##      Executable filename is : getquote2-noxlsx
## JSON data from CoinMarketCAP
## Disply output to screen 
##
## Author: Adrian Lai / Date: 2021-12-06
##
from requests import Request, Session
from datetime import datetime

import pprint
import json


## CMC QUERY API ##<<------------------------------------
apiendpoint_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

## xapiendpoint_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC,LTC,CAKE,BNB'
#apikey = 'b24cd75d-db93-4ed2-9a17-f13c4e810c17'
apikey = 'b24cd75d-db93-4ed2-9a17-f13c4e810c17'

querycoins = { 
               'symbol':'LTC,CAKE,BNB,CRO,DFI,BTC,MATIC' }
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': str(apikey)
}

session = Session()
session.headers.update(headers)

## Get CMC quote data with API key ##
apidata = session.get(apiendpoint_url, params=querycoins)
#apidata = session.get(apiendpoint_url)
#pprint.pprint(json.loads(apidata.text))    ##<--- print if need to debug 

dataall = json.loads(apidata.text)['data']

#bnbprice = json.loads(apidata.text)['data']['BNB']['quote']['USD']['price']
#print("  --->> " + str(bnbprice) + " <---")

data = dataall
#pprint.pprint(data)                          ## Print JSON data read from file :/cmcdata.json


## Currency Rate Query API ##<<------------------------------------
api_exch_url = 'https://freecurrencyapi.net/api/v2/latest?apikey=1b45ee90-501b-11ec-8902-3377424281a1&base_currency=USD'

headers = {
    'Accepts': 'application/json'}

session = Session()
session.headers.update(headers)
exchngrates = session.get(api_exch_url)

#pprint.pprint(json.loads(exchngrates.text))
exUSDSGD = json.loads(exchngrates.text)['data']['SGD']
exSGDUSD = round(1/exUSDSGD, 4)
print('\n\n\n##----------------EXCHANGE RATE-------------------##')
print('\n  SGD-USD rate = $' + str(exUSDSGD) + 
      ' ** USD-SGD = $' + str(exSGDUSD) + ' ** \n')

## Get and display current date time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print('\n#================================================#')
print('$$  Current Price as of :', dt_string + '   $$')
print('#================================================#')

## Read json data file into python object
## with open("./cmcdata1.json") as access_json:
##      readjson = json.load(access_json)
##
#data = readjson['data']


for coinsymbol in data:
#    print(coinsymbol)
    nest1 = data[coinsymbol]
    tokensymbol = coinsymbol
#    print("  --->>>>> data[coinsymbol] value <<<<<---  ")
#    print(nest1)
#    print('\n')
#    quoteUSDprice = str(nest1['quote']['USD']['price'])
    quoteUSDprice = nest1['quote']['USD']['price']
#    perchg1h = str(nest1['quote']['USD']['percent_change_1h'])
    perchg1h = nest1['quote']['USD']['percent_change_1h']
#    perchg24h = str(nest1['quote']['USD']['percent_change_24h'])
    perchg24h = nest1['quote']['USD']['percent_change_24h']
#    perchg30d = str(nest1['quote']['USD']['percent_change_30d'])
    perchg30d = nest1['quote']['USD']['percent_change_30d']
    coinID = nest1['id']
#    print('id: ' + str(nest1['id']) + ' 1h% :' + str(nest1['quote']['USD']['percent_change_1h']) +'\n' )
#    print('id: ' + str(nest1['id']) + ' 24h% :' + str(nest1['quote']['USD']['percent_change_24h']) + '\n' )
#    print('id: ' + str(nest1['id']) + ' 7d% :' + str(nest1['quote']['USD']['percent_change_7d']) + '\n' )
#    print(coinsymbol)                     ## Print retrived Nested json data
#    print("  --->>>>>                  <<<<<---  ")
    curr_price = round(quoteUSDprice,2)
    curr_priceSGD = round(quoteUSDprice*exUSDSGD,2)
    perchg1h = round(perchg1h,2)
    perchg24h = round(perchg24h,2)
    perchg30d = round(perchg30d,2)
    print('CURR Price of ' + tokensymbol + ' is US$' + str(curr_price) +
                          ' / S$' + str(curr_priceSGD) +
                          ' Changes last 1h/24h/30d  : ' + str(perchg1h) + '% / ' + str(perchg24h) +'% / ' + 
                          str(perchg30d) + '% <<< ----------\n') 

