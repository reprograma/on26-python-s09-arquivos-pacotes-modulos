import csv

alunos = [['Chimichanga', '1', 10], ['Tori','6', 10], ['Victor', '30', 0]]

with open('notasAlunos.csv', 'w', newline='') as notas_csv:
    escritor_csv = csv.writer(notas_csv)
    escritor_csv.writerows(alunos)

with open('notasAlunos.csv', 'r', newline='') as notas_csv:
    leitor_csv = csv.reader(notas_csv)

    total_notas = 0
    total_alunos = 0

    for linha in leitor_csv:
        nome, idade, nota = linha
        nota = float(nota)
        total_notas += nota
        total_alunos += 1

    media = total_notas / total_alunos
    print (media)



