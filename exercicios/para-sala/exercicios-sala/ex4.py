import csv

livros = []

while True:
    titulo = input("Digite o titulo do livro ou a palavra sair:")
    if titulo.lower() == 'sair':
        break
    autor = input("Digite o nome do autor:")
    ano = input("Digite o ano de publicação: ")
    livros.append([titulo, autor, ano])

with open ('livros.csv', 'w', newline='') as arq:
    escrita = csv.writer(arq)
    escrita.writerows(livros)

print('informação incluída com sucesso')