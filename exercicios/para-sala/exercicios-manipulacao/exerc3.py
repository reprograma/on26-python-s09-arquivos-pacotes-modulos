'''
*Exercício 3: Leitura e manipulação de um arquivo CSV**

Crie um arquivo CSV chamado "alunos.csv" com informações fictícias de alunos, como nome, idade e nota.
Escreva um programa em Python que leia o arquivo CSV, calcule a média das notas e exiba-a na tela.
'''

import csv

with open('alunos.csv', 'r') as arq:
    leitor_csv = csv.reader(arq)


    total_notas = 0
    total_alunos = 0

    for linha in leitor_csv:
        nome, idade, nota = linha
        nota = float(nota)           # convertendo a variavel nota
        total_notas += nota
        total_alunos += 1

    if total_alunos > 0:
        media = total_notas / total_alunos
        print(f'\n Média das notas dos alunos: {media:.1f} ')

    else:
        print('\n Não há alunos no arquivo')