# import csv

# with open ('./dados.txt', 'r') as file:
#     content = file.read()
#     print(content)

# dados = [['nome', 'idade']], [['Alice', 30]], [['Bob', 25]]

# with open('pessoas.csv', 'w', newline='') as arq_csv:
#     escritor_csv = csv.writer(arq_csv)
#     escritor_csv.writerows(dados)

# with open('pessoas.csv', 'r', newline='') as arq:
#     leitor_csv = csv.reader(arq)
#     for linha in leitor_csv:
#         print(linha)

# import json

# dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}, {'nome': 'Larissa', 'idade': 25, 'cidade': 'Guaruja'}

# with open('dados.json', 'w') as arquivo_json:
#     json.dump(dados, arquivo_json)

# with open('dados.json', 'r') as arquivo_json:
#     dados = json.load(arquivo_json)
#     print(dados)

import csv

with open('./alunos.csv', 'w') as arq_csv:
    leitor_csv = csv.reader(arq_csv)
    



