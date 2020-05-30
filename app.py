from flask import Flask,request,jsonify,render_template
import json
import requests
import os
from tabulate import tabulate
from main import InstaBot

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def post():
	name =request.form['Username']
	password=request.form['Password']
	my_bot = InstaBot(name,password)
	output = my_bot.get_unfollowers()
	return render_template('index.html', output=output)

if( __name__ == '__main__'):
	app.run(debug=True)