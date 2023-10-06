import csv

livros =[]

#recuperar os dados do arquivo livros.csv

with open('livros.csv', 'r') as arq:
    leitor = csv.reader(arq)
    for linha in leitor:
        titulo, autor, ano = linha
        livros.append([titulo, autor, ano])
#input das informações
while True:
    titulo = input('Digite o titulo do livro ou a palavra sair:')
    if titulo.lower() == 'sair':
        print('Saindo do programa...')
        break
    autor = input('Digite o nome do autor: ')
    ano = input('digite o ano de publicação: ')
    livros.append([titulo, autor, ano])

#Salvar os dados que ficou em lista livro =[]

with open('livros.csv', 'w', newline='') as arq:
    escrita = csv.writer(arq)
    escrita.writerows(livros)

if titulo.lower() != 'sair':
    print('informação incluida com sucesso')