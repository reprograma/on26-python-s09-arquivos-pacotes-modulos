import csv

soma_notas = 0 # inicializa a variável para a soma das notas, aqui ele começa com zero pois depois ira incrementando o numero necessário. 

contador_alunos = 0 


with open("./alunos.csv", mode='r') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
                    #o dictreader é feito para ler e grava a informação do arquivo_csv
    for coluna in leitor_csv:
        nota = float(coluna[" nota"])
        soma_notas += nota
        contador_alunos += 1

# Calcula a média das notas
media_notas = soma_notas / contador_alunos

print(f'* Média das Notas dos Alunos *')
print(f'Número total de alunos: {contador_alunos}')
print(f'Soma das notas: {soma_notas:.2f}')
print(f'Média das notas: {media_notas:.2f}')


    

   

