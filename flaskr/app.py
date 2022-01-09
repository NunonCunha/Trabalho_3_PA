import random
import json
from flask import Flask, render_template, request
from flask.wrappers import Request


'''Variáveis'''

#Variavel para o random
indice = 0
#recebe todas as perguntas vindas do ficheiro json
lista_perguntas = []
#recebe todas as respostas vindas do ficheiro json
lista_respostas = []
#lista para validar os números random gerados, de forma a não haver repetições
lista_indice = []
#Lista de perguntas randomizadas
perguntasRandom = []
#Lista de respostas randomizadas
respostasRandom = []
#Lista temporária para validar as respostas submetidas
respostasTemp = []
#contador para as respostas certas
respostasCertas = 0
#Dicionário para receber as respostas do utilizador
respostas = {}
falhadas = 5*[None]



'''Funções'''

# Tratamento do Ficheiro
def trataFicheiro():
    try:
        file = open('perguntas.json', encoding='utf-8') 
        perguntas = json.load(file)
        print("Ficheiro aberto com sucesso...")
    except:
        print("Não foi possivel abrir o ficheiro")

    #passa as perguntas do ficheiro json para uma lista de perguntas
    for pergunta in perguntas.keys():
        lista_perguntas.append(pergunta)
    #passa as respostas do ficheiro json para uma lista de perguntas
    for resposta in perguntas.values():        
        lista_respostas.append(resposta)

    file.close()

#Random Perguntas
def randomPR():
    
    trataFicheiro()
    '''
    for i in range(5):
        #Random do indice das perguntas com o range do tamanho do ficheiro
        indice = random.randint(0, len(lista_perguntas)-1)
        if indice in lista_indice:
            #caso o indice já exista na lista, é randomizado um número até não se repetir
            indice = random.randint(0, len(lista_perguntas)-1)
            perguntasRandom.append(lista_perguntas[indice])
            respostasRandom.append(lista_respostas[indice])
        else:
            lista_indice.append(indice)
            perguntasRandom.append(lista_perguntas[indice])
            respostasRandom.append(lista_respostas[indice])
    '''

    while len(lista_indice) < 5:
        indice = random.randint(0, len(lista_perguntas)-1)
        if indice in lista_indice:
            #caso o indice já exista na lista, é randomizado um número até não se repetir
            indice = random.randint(0, len(lista_perguntas)-1)
            # perguntasRandom.append(lista_perguntas[indice])
            # respostasRandom.append(lista_respostas[indice])
        else:
            lista_indice.append(indice)
            perguntasRandom.append(lista_perguntas[indice])
            respostasRandom.append(lista_respostas[indice])


   

#Tratamento de respostas
def tratamentoRespostas(res):
    
    respostasCertas = 0
    
    for resposta in res.values():        
        respostasTemp.append(resposta)

    for i in range(5):
        if respostasRandom[i] == respostasTemp[i]:
            respostasCertas += 1
            falhadas[i] = ""
        else:
            falhadas[i] = perguntasRandom[i]

    return respostasCertas

    

#Criação da aplicação Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get():

    randomPR()
    return render_template("quiz.html", Pergunta1 = perguntasRandom[0], Pergunta2 = perguntasRandom[1], Pergunta3 = perguntasRandom[2], Pergunta4 = perguntasRandom[3], Pergunta5 = perguntasRandom[4])
    

@app.route("/", methods=['post'])
def post():

    respostas = request.form
    tratamentoRespostas(respostas)
    result = tratamentoRespostas(respostas)
 
    return render_template("resultado.html", resultado = result, fail1 = falhadas[0], fail2 = falhadas[1], fail3 = falhadas[2], fail4 = falhadas[3], fail5 = falhadas[4] )

if __name__ == "__main__":

    app.run(debug=True, port=8080)
