import csv
with open('./dados.txt', 'r') as arquivos: #read
    #conteudo = arq.read()
    conteudo = arquivos.read()
    print (conteudo)

    linhas = arquivos.readlines()
    #print(linhas)
    print(linhas)
    #linha = arq.readline() #
    #print(linha)
with open('./dados1.txt', 'w') as arquivo:
        arquivo.write("fim de linha")

dados = [['nome', 'idade'],['alice',30], ['bob', 25]]

#with open ('pessoas.csv', 'w', newline= '') as arq_csv:
  #escritor_csv = csv.writer(arq_csv)
  #escritor_csv.writerows(dados)

with open('pessoas.csv', 'r', newline='') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)

import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)


import json

with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)