import json

dados = {
    'Livro': 'Anne de Green Gables', 
    'autor': 'L. M. Montgomery', 
    'Ano_Publicacao': 1908,
}

with open('newdados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

with open ('newdados.json', 'r') as arquivo_json:
    dados  = json.load(arquivo_json)
    print(dados)
