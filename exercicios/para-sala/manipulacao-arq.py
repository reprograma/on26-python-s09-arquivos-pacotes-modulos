import csv


''' 'r' = read

with open('./dados.txt', 'r') as arquivos:
    conteudo = arquivos.read()
    print(conteudo)


# retornando o conteudo e as linhas como uma lista
with open('./dados.txt', 'r') as arquivos:
    linhas = arquivos.readlines()
    print(linhas)

# 'w' = write

with open('./dados-write.txt', 'w') as arquivo:
    arquivo.write("fim de linha")


dados = [['Nome', 'Idade'], ['Alice', 30], ['Bob', 25]]

with open('pessoas.csv', 'w', newline='') as arq_csv:
    escritor_csv = csv.writer(arq_csv)
    escritor_csv.writerows(dados)

with open('pessoas.csv', 'r') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)

'''



import json

'''
dados = {'Nome': 'Alice', 'Idade': 30, 'Cidade': 'Recife'}, {'Nome': 'Maria', 'Idade': 15, 'Cidade': 'Cabo'}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)
'''

with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
