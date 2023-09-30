'''
**Exercício 2: Escrita em um arquivo JSON**

Crie um dicionário Python com alguns dados e escreva-o em um arquivo JSON chamado "pets.json".
Em seguida, leia o arquivo JSON e exiba os dados lidos.

'''

import json

pets = {'Nome': 'Coroninha', 'Idade': 3, 'Cidade': 'Recife'}, {'Nome': 'Bisbi', 'Idade': 5, 'Cidade': 'Uberlandia'}

with open('pets.json', 'w') as arq_json:
    json.dump(pets, arq_json)

with open('pets.json', 'r') as arq_json:
    pets = json.load(arq_json)
    print(pets)

