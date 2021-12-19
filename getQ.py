from flask import Flask, Blueprint, render_template, request, flash, Markup
from requests import Request, Session
from datetime import datetime
#from backports import zoneinfo

from queryCMC import getCMCquotesRESTapi, getSGDUSDrate

import json
import pprint
import pytz

app = Flask(__name__)
#app.secret_key = "showmethemoney168"


views = Blueprint(__name__, "views")
viewq = Blueprint(__name__, "viewq")

@views.route("/")
def home():
	msg1 = Markup('###  Version 1.0 HOME Page - This version only displays my favourite Crypto Tokens <br>')
	msg2 = Markup('###     next version will display the tokens you entered below <br>')
	flash(msg1 + msg2)
	return render_template("index.html", favcoins="CRO,CAKE,LTC,MATIC,BNB", curr="SGD")
#	return "home getq page"

@views.route("/viewq", methods=["POST"])
def altcoins():
#
#	Get Exchange Rates
#
	exUSDSGD = getSGDUSDrate()
	exSGDUSD = round(1/exUSDSGD, 4)
#
#	Get Current Date/time
#
	tz = pytz.timezone('Asia/Manila')
	now = datetime.now(tz)

	dt_string = now.strftime("%d/%m/%Y Timezone GMT+8 : %H:%M:%S")
	fc = request.form['coin_input'] 
	cmcquotes = getCMCquotesRESTapi(exUSDSGD)
	if cmcquotes == None:
		msg0 = Markup('You need to get your own API_KEY from https://pro.coinmarketcap.com/signup/  <br>')
		msg1 = Markup('to run this program. <br>')
		msg2 = Markup('Input your API KEY from CMC into  .env file in the same directory as your python script <br><br><br>')
		msg3 = Markup('Format: <span class="tab"></span> cmcAPI_KEY=abcdefuuuddddkkkkgggadkfhakdj  <br><br><br>')
		msg4 = Markup('<em>Note: without quotes and CR </em> <br>')
		flash(msg0 + msg1 + msg2 + msg3 + msg4)
		return render_template("noAPIKEY.html")
	else:
		msg1 = Markup('Quotes from CMC as follows    <span class="tab"></span>   <span class="tab"></span>       Changes last 1h / 24h / 30d ')
		flash(msg1 + cmcquotes)
		return render_template("dispquotes.html", exrate1=str(exUSDSGD), exrate2=str(exSGDUSD), currDT=dt_string, userinput=str(fc))

@app.route("/viewxxxx")
def index():
	flash("VIEWQ version - CMC quotes of favourite coins to display here....!!! ")
	return render_template("index.html", favcoins="BTC,XRP,ADA,SOL", curr="SGD")

@app.route("/greet", methods=["POST", "GET"])
def getcmcq():
	flash("Your favourite coins are : " + str(request.form['favcoins']) + "..hahaha. ")
	return render_template("index.html")