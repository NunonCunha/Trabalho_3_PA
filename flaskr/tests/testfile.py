import json
import random


#Variáveis
indice = 0
lista_perguntas = []
lista_respostas = []
lista_indice = []
respostas = { "pergunta1": "verdadeiro", "pergunta2": "falso", "pergunta3": "verdadeiro", "pergunta4": "falso", "pergunta5": "verdadeiro"}
perguntasRandom = []
respostasRandom = []
respostasTemp = []
respostasCertas = 0

 
def trataFicheiro():
    try:
        file = open('perguntas.json', encoding='utf-8') 
        perguntas = json.load(file)
        print("Ficheiro aberto com sucesso...")
    except:
        print("Não foi possivel abrir o ficheiro")


    for pergunta in perguntas.keys():

        lista_perguntas.append(pergunta)

    for resposta in perguntas.values():
        
        lista_respostas.append(resposta)

    file.close()

def randomPR():
    trataFicheiro()
    for x in range(5):
        indice = random.randint(0, len(lista_perguntas)-1)
        if indice in lista_indice:
            indice = random.randint(0, len(lista_perguntas)-1)
            perguntasRandom.append(lista_perguntas[indice])
            respostasRandom.append(lista_respostas[indice])
        else:
            lista_indice.append(indice)

            perguntasRandom.append(lista_perguntas[indice])
            respostasRandom.append(lista_respostas[indice])


def tratamentoRespostas(res):

    respostasCertas = 0
    
    for resposta in res.values():        
        respostasTemp.append(resposta)

    for i in range(5):
        if respostasRandom[i] == respostasTemp[i]:
            respostasCertas += 1
    return respostasCertas


randomPR()
acertou = tratamentoRespostas(respostas)

print(acertou)
