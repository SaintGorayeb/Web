from flask import Flask

app = Flask(__name__)

def somar(a, b):
    return a + b

@app.route('/home')
def home():
    soma = somar(5,2)
    return 'Helloween'

if __name__ == "__main__":
    app.run(debug = False)

