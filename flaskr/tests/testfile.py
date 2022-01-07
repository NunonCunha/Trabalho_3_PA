import json
import random



indice = random.randint(0, 15)
lista_perguntas = []
lista_respostas = []
lista_indice = []
 
try:
    with open('perguntas.json', encoding='utf-8') as f:
        perguntas = json.load(f)
        print("Ficheiro aberto com sucesso...")
except:
    print("Não foi possivel abrir o ficheiro")


for pergunta in perguntas.keys():

    lista_perguntas.append(pergunta)

for resposta in perguntas.values():
    
    lista_respostas.append(resposta)


for x in range(5):
    indice = random.randint(0, 15)
    if indice in lista_indice:
        indice = random.randint(0, 15)
        print(lista_perguntas[indice])
        print(lista_respostas[indice])
    else:
        lista_indice.append(indice)

        print(lista_perguntas[indice])
        print(lista_respostas[indice])



