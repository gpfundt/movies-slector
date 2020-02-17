from flask import Flask, render_template
from flask import request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    console.log('WOooooooo')

@app.route('/test', methods=['GET', 'POST']) 
def test():
    print(request.get_json())
    return "TEST"