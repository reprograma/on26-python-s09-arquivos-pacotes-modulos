import csv

#with open('./dados.txt', 'r') as arq:
    #conteudo = arq.read()
    #print(f'{conteudo} - Professora')
    #linhas = arq.readlines()
    #print(linha)
    #print(linhas[1])
    #linha = arq.readline()
    #print(linha)

#with open('./dados8.txt', 'w') as arquivo:
    #arquivo.write("fim de linha")

#dados = [['nome', 'Idade'], ['Alice', 30], ['bob', 25]]

#with open('pessoas.csv', 'w', newline='') as arq_csv:
    #escritor_csv = csv.writer(arq_csv)
    #escritor_csv.writerows(dados)

with open('pessoas.csv', 'r', newline='') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)

import json

dados = [{'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'},{'nome': 'Maria', 'idade': 22, 'cidade': 'Exemploville'}]


with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

