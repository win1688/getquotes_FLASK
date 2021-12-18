from flask import Flask, Blueprint, render_template, request, flash, Markup
from requests import Request, Session
from datetime import datetime

from queryCMC import getCMCquotesRESTapi, getSGDUSDrate

import json
import pprint

app = Flask(__name__)
#app.secret_key = "showmethemoney168"


views = Blueprint(__name__, "views")
viewq = Blueprint(__name__, "viewq")

@views.route("/")
def home():
	msg1 = Markup('###  Version 0.9a HOME Page - This version only displays my favourite Crypto Tokens <br>')
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
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y Timezone GMT+8 : %H:%M:%S")
	fc = request.form['coin_input'] 
	paramsg = getCMCquotesRESTapi(exUSDSGD)
	flash("Quotes from CMC as follows  " + paramsg)
	return render_template("dispquotes.html", exrate1=str(exUSDSGD), exrate2=str(exSGDUSD), currDT=dt_string, userinput=str(fc))

@app.route("/viewxxxx")
def index():
	flash("VIEWQ version - CMC quotes of favourite coins to display here....!!! ")
	return render_template("index.html", favcoins="BTC,XRP,ADA,SOL", curr="SGD")

@app.route("/greet", methods=["POST", "GET"])
def getcmcq():
	flash("Your favourite coins are : " + str(request.form['favcoins']) + "..hahaha. ")
	return render_template("index.html")