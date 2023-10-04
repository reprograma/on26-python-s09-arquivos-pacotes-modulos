#**Exercício 2: Escrita em um arquivo JSON**

#Crie um dicionário Python com alguns dados e escreva-o em um arquivo JSON chamado "dados.json". 
#Em seguida, leia o arquivo JSON e exiba os dados lidos.

import json

dados = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'Sao Paulo'
}

with open('dados.json', 'w') as arq:
    json.dump(dados, arq)

with open('dados.json', 'r') as arq:
    dados_lidos = json.load(arq)
    print(dados_lidos)