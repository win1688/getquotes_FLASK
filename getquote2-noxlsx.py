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

## CMC API
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


## Currency Rate API
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

dataall = json.loads(apidata.text)['data']
data = dataall


#print(data)                          ## Print JSON data read from file :/cmcdata.json

for lv01 in data:
#    print(lv01)
    nest1 = data[lv01]
    tokensymbol = lv01
#    print(nest1)                     ## Print retrived Nested json data
    date_updated = nest1['last_updated']
    for lv02 in nest1:
        nest2 = nest1[lv02]
        tp = json.loads(data)['last_updated']['BTC']['USD']
        print('  ## ' + tp + ' ## \n')
        if 'name' in lv02:
            tokenname = nest1[lv02]
#            tokendetails = json.loads(nest1.text)[tokensymbol]
#            print('\n lv02 ' + lv02 + '   \n')
#            print('\n==============> ' + tokenname + ' <=============')
        if 'quote' in lv02:
            for lv03 in nest2:
                nest3 = nest2[lv03]
#                print(nest3)            ## Inner most NESTED Dict [price info]
                if 'USD' in lv03:
                    curr_price = round(nest3['price'],2)
                    curr_priceSGD = round(nest3['price']*exUSDSGD,2)
                    perchg1h = round(nest3['percent_change_1h'],2)
                    perchg24h = round(nest3['percent_change_24h'],2)
                    perchg30d = round(nest3['percent_change_30d'],2) 
                    perchg24hEx = round(nest3['percent_change_24h'],2)/100
                    perchg30dEx = round(nest3['percent_change_30d'],2)/100 
                    print('CURR Price of ' + tokensymbol + ' is US$' + str(curr_price) +
                          ' / S$' + str(curr_priceSGD) +
                          ' Changes last 1h/24h/30d  : ' + str(perchg1h) + '% / ' + str(perchg24h) +'% / ' + 
                          str(perchg30d) + '% <<<----------\n')
                    curr_row = [tokenname, tokensymbol, curr_price, curr_priceSGD, perchg24hEx, perchg30dEx, date_updated]







