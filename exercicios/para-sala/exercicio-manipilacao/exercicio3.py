        

import csv

with open('alunos.csv', 'r') as arq:
    leitor_csv = csv.reader(arq)
    total_notas = 0
    total_alunos = 0
    for linha in leitor_csv:
        nome, idade, nota = linha # colunas csv nome, idade, nota
        nota = float(nota)
        total_notas += nota
        total_alunos += 1
        
    if total_alunos > 0:
        media = total_notas/total_alunos
        print(f'medias das notas: {media}') 
    else:
        print('Não há alunos na sala')
        

