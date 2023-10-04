import csv

# Abre o arquivo "alunos.csv" no modo leitura ('r') usando a biblioteca csv.
# O arquivo CSV deve conter linhas com nome, idade e nota de alunos.
with open('alunos.csv', 'r', newline='') as arq:
    leitor_csv = csv.reader(arq)
    
    total_notas = 0  # Inicializa a soma total das notas dos alunos.
    total_alunos = 0  # Inicializa o contador de alunos.
    nota = 0  # Variável temporária para armazenar a nota de cada aluno.
    
    # Itera pelas linhas do arquivo CSV.
    for linha in leitor_csv:
        nome, idade, nota = linha
        nota = float(nota)  # Converte a nota de string para float.
        total_notas += nota  # Adiciona a nota à soma total das notas.
        total_alunos += 1  # Incrementa o contador de alunos.
        
    # Calcula a média das notas dos alunos, se houver alunos no arquivo.
    if total_alunos > 0:
        media = total_notas / total_alunos
        print(f'Média das notas: {media}')
    else:
        print('Não existem alunos')  # Exibe uma mensagem se não houver alunos no arquivo.
