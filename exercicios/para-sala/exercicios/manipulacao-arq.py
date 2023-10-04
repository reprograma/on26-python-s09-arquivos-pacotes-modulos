# with open ('./dados.txt', 'r') as arquivos: #read
#   # conteudo = arquivos.read() #receber essas infos
#   #print(f'{conteudo} - Professora)
#   linhas = arquivos.readlines() #Executa todas as linhas em lista. O número que tá ali dentro fará aparecer a posição
#   print(linhas[2])
#   # linha = arquivos.readline() #Executa certo caractere que está dentro dos parenteses
#   # print(linha)
# O código abaixo escreve algo num arquivo já feito previamente chamado dados1
# with open ('./dados1.txt', 'w') as arquivo:
#   arquivo.write('fim de linha')

# #w = write, r = read
#as linhas abaixo escrevem e transportam para uma row
import csv

# dados = [['nome', 'idade'], ['alice', 30], ['bob', 35]]

# with open('pessoas.csv', 'w', newline='') as arq_csv:
#   escritor_csv = csv.writer(arq_csv)
#   escritor_csv.writerows(dados)

# #itera a lista
# with open ('pessoas.csv', 'r', newline='') as arq:
#   leitor_csv = csv.reader(arq)
  # for linha in leitor_csv:
#     print(linha)  

import json
dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'exemploville'}, {'nome': 'Amanda', 'idade': 25, 'cidade': 'strangeville'}

with open ('dados.json', 'w', newline='') as arquivo_json: #ele cria o arquivo dados.json e coloca os dados dentro do arquivo
  json.dump(dados, arquivo_json)
