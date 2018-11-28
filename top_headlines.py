from flask import Flask, render_template, url_for
import requests
from secrets_example import *
import json

app = Flask(__name__)

@app.route('/user/<word>')
def user_page(word):
	baseurl ='https://api.nytimes.com/svc/topstories/v2/'
	section = 'technology'
	extendedurl = baseurl + section +'.json'
	params = {'api-key': api_key}
	results = requests.get(extendedurl, params).json()
	results = results['results']

	res = []
	res = [{'title':i['title'],'url':i['url']} for i in results][:5]

	return render_template('user.html', name = word, topic = section, news = res)

@app.route('/')
def index():
    return render_template('welcome.html')

if __name__ == '__main__':
	app.run(debug=True)