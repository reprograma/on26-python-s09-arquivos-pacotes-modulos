import csv

livros = []

with open('livros.csv', 'r') as arq:
    leitor = csv.reader(arq)
    for linha in leitor:
        titulo, autor, ano = linha
        livros.append([titulo, autor, ano])

while True:
    titulo = input("digite o título do livro ou a palavra sair:")
    if titulo.lower() == 'sair':
        print("saindo do programa....")
        break
    autor = input("digite o nome do autor: ")
    ano = input("digite o ano de publicação: ")
    livros.append([titulo, autor, ano])
    

with open('livros.csv', 'w', newline='') as arq:
    escrita = csv.writer(arq)
    escrita.writerows(livros)
   
if titulo.lower() != 'sair': 
    print('informação incluida com sucesso')