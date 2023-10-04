import json

#fazer dicionario={"a":"amor","idade: 2"}
dados = {'pet ': 'Morgana', 'idade': 3 , 'cidade': 'sjc'}


#aqui cria arquivo =>'w'
with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json) 

#aqui ler o aquivo criado ="r" 
with open('dados.json', 'r') as arq:
    dados_lidos = json.load(arq)
    print(dados_lidos)