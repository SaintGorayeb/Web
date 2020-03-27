from flask import Flask

app = Flask(__name__)

def somar(a, b):
    return a + b

@app.route('/ValbertoEnxamista')

def home():
    soma = somar(5,2)
    return 'Hello World'

app.run(debug = False)

