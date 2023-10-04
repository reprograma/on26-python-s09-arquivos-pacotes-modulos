#Exercício 1
# Crie um arquivo de texto chamado "dados.txt" com algumas linhas de texto. Escreva um programa em Python que leia o conteúdo do arquivo e exiba-o na tela.

# with open ('dados.txt', 'r',newline='') as dados:
#   conteudo = dados.read()
#   print(conteudo)


# # **Exercício 2: Escrita em um arquivo JSON**
# # Crie um dicionário Python com alguns dados e escreva-o em um arquivo JSON chamado "dados.json". Em seguida, leia o arquivo JSON e exiba os dados lidos.

# import json
# dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'exemploville'}, {'nome': 'Amanda', 'idade': 25, 'cidade': 'strangeville'}

# with open ('dados_exercicio2.json', 'w', newline='') as dados_json:
#   json.dump(dados, dados_json)

# **Exercício 3: Leitura e manipulação de um arquivo CSV**
# Crie um arquivo CSV chamado "alunos.csv" com informações fictícias de alunos, como nome, idade e nota. Escreva um programa em Python que leia o arquivo CSV, calcule a média das notas e exiba-a na tela.

import csv
with open ('alunos.csv', 'r') as arq:
  leitor_csv = csv.reader(arq)
  total_alunos = 0
  total_notas = 0
  for line in leitor_csv:
    nome, idade, nota = line
    nota = float(nota)
    total_notas = total_notas + nota
    total_alunos = total_alunos + 1

    if total_alunos > 0:
      media = total_notas/total_alunos
      print(f'a média das notas é {media:.1f}')
    else:
      print('valor inválido')