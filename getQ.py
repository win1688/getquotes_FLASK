from flask import Flask, Blueprint, render_template, request, flash
from requests import Request, Session

import json
import pprint

app = Flask(__name__)
#app.secret_key = "showmethemoney168"


views = Blueprint(__name__, "views")
viewq = Blueprint(__name__, "viewq")

@views.route("/")
def home():
	flash(" ###  HOME Dir - CMC quotes of favourite coins to display here....!!! ")
	return render_template("index.html", favcoins="CRO,CAKE,LTC,MATIC,BNB", curr="SGD")
#	return "home getq page"

@views.route("/viewq", methods=["POST"])
def altcoins():
#
#	Get Exchange Rates
#
	api_exch_url = 'https://freecurrencyapi.net/api/v2/latest?apikey=1b45ee90-501b-11ec-8902-3377424281a1&base_currency=USD'
	headers = {'Accepts': 'application/json'}
	session = Session()
	session.headers.update(headers)
	exchngrates = session.get(api_exch_url)
	pprint.pprint(json.loads(exchngrates.text))
	exUSDSGD = json.loads(exchngrates.text)['data']['SGD']
	exSGDUSD = round(1/exUSDSGD, 4)
	exratetext = ' ** SGD-USD rate = $' + str(exUSDSGD) + ' ** USD-SGD = $' + str(exSGDUSD) + ' ** '
#
	fc = request.form['coin_input'] 
#
#
	flash("VIEWQ Dir - Your favourite coins are : " + str(fc) + exratetext)
	return render_template("dispquotes.html", favcoins=str(fc), curr="EUR")



@app.route("/viewxxxx")
def index():
	flash("VIEWQ version - CMC quotes of favourite coins to display here....!!! ")
	return render_template("index.html", favcoins="BTC,XRP,ADA,SOL", curr="SGD")

@app.route("/greet", methods=["POST", "GET"])
def getcmcq():
	flash("Your favourite coins are : " + str(request.form['favcoins']) + "..hahaha. ")
	return render_template("index.html")