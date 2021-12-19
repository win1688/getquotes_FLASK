from flask import Flask, Blueprint, request, flash
from getQ import views, viewq


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.secret_key = "showmethemoney168"


if __name__ == "__main__":
	app.run(port=80)

