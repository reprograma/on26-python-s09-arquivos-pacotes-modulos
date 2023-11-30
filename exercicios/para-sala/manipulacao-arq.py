import csv

# with open('./dados.txt', 'w') as arquivos: #read
#     # # conteudo = arquivos.read()
#     # # print (f' {conteudo} - Aluna Atrasada')

#     # # linha = arquivos.readline()
#     # linhas = arquivos.readlines()

#     # # print(linha)
#     # print(linhas[2])

#     arquivos.write("fim de linha")

# informacoes = [['nome', 'idade'], ['Chimichanga', '1'], ['Tori','6'], ['Victor', '30']]

# with open('planilha.csv', 'w', newline='') as planilha_csv:
#     escritor_csv = csv.writer(planilha_csv)
#     escritor_csv.writerows(informacoes)

# with open('planilha.csv', 'r', newline='') as planilha_csv:
#     leitor_csv = csv.reader(planilha_csv)
#     for linha in leitor_csv:
#         print(linha)

import json

informacoes = {'nome': 'Chimichanga', 'idade': 1, 'raca':'Salchihuahua'}

# with open('planilha.json', 'w') as planilha_json:
#     json.dump(informacoes, planilha_json)

with open('planilha.json', 'r') as planilha_json:
    informacoes = json.load(planilha_json)
    print(informacoes)

