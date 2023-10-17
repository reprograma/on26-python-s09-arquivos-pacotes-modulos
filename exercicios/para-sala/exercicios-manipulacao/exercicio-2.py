import json

dados = {
    'nome': 'Joao',
    'idade': 31,
    'cidade': 'Santo Andre'
}

with open ('dados.json', 'w') as arq:
    json.dump(dados, arq)

with open ('dados.json', 'r') as arq:
    dados_lidos = json.load(arq)
    print(dados_lidos)