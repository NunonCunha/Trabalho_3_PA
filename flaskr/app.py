#biblioteca para gerar objectos de forma randomizada
import random
#biblioteca para tratamento de ficheiros do tipo json
import json
#biblioteca do Flask para desenvolvimento web
from flask import Flask, render_template, request

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
#lista de respostas falhadas
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
    
    #Chamada da função para iniciar o tratamento do ficheiro
    trataFicheiro()

    while len(lista_indice) < 5:
        indice = random.randint(0, len(lista_perguntas)-1)
        if indice in lista_indice:
            #caso o indice já exista na lista, é randomizado um número até não se repetir
            indice = random.randint(0, len(lista_perguntas)-1)

        #Adiciona as referidas listas as perguntas e respostas randomizadas
        else:
            lista_indice.append(indice)
            perguntasRandom.append(lista_perguntas[indice])
            respostasRandom.append(lista_respostas[indice])
   

#Tratamento de respostas
def tratamentoRespostas(res):
    
    respostasCertas = 0
    
    #Guarda na lista de respostas as respostas dadas pelo cliente atraves do form
    for resposta in res.values():        
        respostasTemp.append(resposta)

    #Loop para validar as respostas certas ou erradas
    for i in range(5):
        if respostasRandom[i] == respostasTemp[i]:
            respostasCertas += 1
            
        else:
            #se a resposta for falhada, quarda a pergunta falhada na lista de falhadas, no html as perguntas falhadas aparecem seguidas
            falhadas[i - respostasCertas] = perguntasRandom[i] 

    #preenche a lista com um valor em branco onde existem valores nulos
    for i in range (len(falhadas)):
        if falhadas[i] == None:
            falhadas[i] = ""

    return respostasCertas
    

#Criação da aplicação Flask
app = Flask(__name__)


#route para apresentar as perguntas geradas aleatoriamente
@app.route("/", methods=['GET'])
def get():

    randomPR()
    return render_template("quiz.html", Pergunta1 = perguntasRandom[0], Pergunta2 = perguntasRandom[1], Pergunta3 = perguntasRandom[2], Pergunta4 = perguntasRandom[3], Pergunta5 = perguntasRandom[4])
    

#route que recebe o POST do form html, trata os dados e mostra o resultado
@app.route("/", methods=['POST'])
def post():
    
    #recebe o dicionário de respostas enviadas pelo cliente
    respostas = request.form
    #passa a variavel para a função de tratamento das respostas
    tratamentoRespostas(respostas)
    #variavel para amostra do resultado do teste
    result = tratamentoRespostas(respostas)
 
    return render_template("resultado.html", resultado = result, fail1 = falhadas[0], fail2 = falhadas[1], fail3 = falhadas[2], fail4 = falhadas[3], fail5 = falhadas[4] )


# Iniciação da aplicação
if __name__ == "__main__":

    app.run(debug=True, port=8080)
