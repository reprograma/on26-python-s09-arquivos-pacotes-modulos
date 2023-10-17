import csv

# with open ('./dados.txt', 'r') as arq: #read
    # conteudo = arq.read()
    # print(f'{conteudo} - Professora')
    # linhas = arq.readlines()
    # print(linhas)
    # print(linhas[1])
    # linha = arq.readline()
    # print(linha)

# with open ('./dados1.txt', 'w') as arquivo:
    # arquivo.write("fim de linha")

# dados = [['Nome', 'Idade'], ['Alice', 30], ['Bob', 24]]
   # escritor_csv = csv.writer(arq_csv)
   # escritor_csv.writerows(dados)

# with open('pessoas.csv', 'w', newline='') as arq_csv:
    # leitor_csv = csv.reader(arq)
    # for linha in leitor_csv:
        # print(linha)

import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}
dados = {'nome': 'Amanda', 'idade': 30, 'cidade': 'Exemploville'}


# with open ('dados.json', 'w') as arquivo_json:
    # json.dump(dados, arquivo_json)

with open ('dados.json', 'r') as arquivo_json:
    json.load(dados, arquivo_json)
    print(dados)