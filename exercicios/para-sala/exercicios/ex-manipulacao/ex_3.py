# <!-- **Exercício 3: Leitura e manipulação de um arquivo CSV**

# Crie um arquivo CSV chamado "alunos.csv" com informações fictícias de alunos, como nome, idade e nota. Escreva um programa em Python que leia o arquivo CSV, calcule a média das notas e exiba-a na tela. -->

import csv

with open('alunos.csv', 'r') as arq: #um loop que irá ler todas as linhas
    leitor_csv = csv.reader(arq)

    total_notas = 0
    total_alunos = 0

    for linha in leitor_csv:
        nome, idade, nota = linha
        nota = float(nota)
        total_notas = total_notas + nota
        total_alunos = total_alunos + 1

    if total_alunos > 0:
        media = total_notas / total_alunos
        print(f'média das notas: {media:.1f}')

    else:
        print('não há alunos no arquivo')

