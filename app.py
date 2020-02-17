<<<<<<< HEAD
import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

#print the response text (the content of the requested file):

print(x.text)
=======
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
>>>>>>> 2147257e5d487e78ab23eef9ad342f82c74ee379
