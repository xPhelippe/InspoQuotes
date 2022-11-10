from flask import Flask
from flask import url_for

app = Flask(__name__)



@app.route('/')
def index():
    return 'index'

@app.route('/addPhone')
def addPhone():
    return 'phone added'

@app.route('/removePhone')
def removePhone():
    return 'phone removed'

@app.route('/todaysQuote')
def getTodaysQuote():
    return "today's quote is..."

