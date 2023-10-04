#from datetime import datetime
import csv
livros = []
#recuperar os dados do arquivo livros.csv
#esse arquivo não funciona se não houver a pasta aberta antes
with open('livros.csv','r') as arq:
    leitor = csv.reader(arq)
    for linha in leitor:
        titulo, autor, ano = linha
        livros.append([titulo, autor, ano])

#input das infos
while True:
    titulo = input('Digite o título do livro ou a palavra sair: ')
    if titulo.lower() == 'sair':
        print('Saindo do programa....')
        break
    autor = input('Digite o nome do autor: ')
    ano = input('Digite o ano de publicação: ')
    livros.append([titulo, autor, ano])

#salvar os dados que ficou em lista livro = []
with open('livros.csv', 'w', newline='') as arq:
     escrita = csv.writer(arq)
     escrita.writerows(livros)



if titulo.lower( ) != 'sair':
    print('Informação incluída com sucesso')