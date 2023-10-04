import json
dados= {
    'nome' : 'Suri',
    'idade': 13,
    'cidade': 'Paulista'
}

with open('dados.json', 'w') as arq:
    json.dump(dados, arq)
    
with open('dados.json', 'r') as arq:
    dados_lido = json.load(arq)
    print(dados_lido)