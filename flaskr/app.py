import codecs
from flask import Flask, render_template, request

# Variáveis
respostas = {}


#Funções

# Tratamento do Ficheiro


#Criação da aplicação Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get():

        return render_template("quiz.html", Pergunta1="esta é uma pergunta vinda do python")



@app.route("/", methods=['post'])
def post():

    respostas = request.form
  
    return respostas


if __name__ == "__main__":

    app.run(debug=True, port=8080)
