# **Exercício 2: Escrita em um arquivo JSON**

# Crie um dicionário Python com alguns dados e escreva-o em um arquivo JSON chamado 
# "dados.json". Em seguida, leia o arquivo JSON e exiba os dados lidos.

import json

alunos = {
    'Aline': 1,
    'Marcos': 2
}
with open('dados.json', 'w') as arq: #cria o json
    json.dump(alunos, arq)
    
    
with open ('dados.json', 'r') as arq: #lê o json
    dados_lidos = json.load(arq)
    print(dados_lidos)
    
   
   