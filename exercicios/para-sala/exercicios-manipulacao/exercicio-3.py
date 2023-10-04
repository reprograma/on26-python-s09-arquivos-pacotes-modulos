import csv #não esquecer de importar a biblioteca

with open('alunos.csv', 'r') as arq:
    leitor_csv = csv.reader(arq)
    
    total_notas = 0
    total_alunos = 0
    
    for linha in leitor_csv:
      linha = nome , idade, nota 
      nota = float(nota)  # Convert nota to a float
      total_notas = total_notas + nota
      total_alunos = total_alunos + 1
        
    if total_alunos > 0:
      media = total_notas / total_alunos
      print(f'média das notas: {media}')
        
    else:
      print('não há alunos no arquivo')




#não esta funcionando