from flask import Flask

app = Flask(__name__)

def somar(a, b):
    return a + b

@app.route('/home')
def home():
    soma = somar(5,2)
<<<<<<< HEAD
    return 'Helloween'
=======
    return 'agora o bicho vai pegar'
>>>>>>> 1173ca85a53387ce3308ec6f5c92f5750a066f7b

if __name__ == "__main__":
    app.run(debug = False)

