import json

dados = {'nome': 'Julia', 'idade': 30, 'cidade': 'Acredita e vai'}

with open('dados.json', 'w') as arq:
    json.dump(dados, arq)
    
with open('dados.json', 'r') as arq:
    dados = json.load(arq)
    print(dados)