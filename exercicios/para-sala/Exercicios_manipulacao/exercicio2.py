import json

dados = {
    'nome': 'Daniele Azevedo',
    'idade': 38,
    'cidade':'Valenca',
    'curso': 'Matematica'
}

with open('dados.json', 'w') as arq:
    json.dump(dados, arq)

with open('dados.json', 'r') as arq:
    dados_lidos = json.load(arq)
    print(dados_lidos)