import json

dicionarioTeste = {
    'nome': 'Victor', 
    'idade': 30, 
    'profissão': 'vendedor'
    }

with open ('dados.json', 'w') as dados_json:
   json.dump(dicionarioTeste, dados_json)

with open('dados.json', 'r') as dados_json:
    dicionarioTeste = json.load(dados_json)
    print(dicionarioTeste)