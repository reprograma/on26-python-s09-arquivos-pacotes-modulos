import csv
livros = []
while True:
  titulo = input ("digite o título do livro ou a palavra sair: ")
  if titulo.lower() == 'sair':
    break 
  autor = input("digite o nome do autor: ")
  ano = input("digite o ano de publicação: ")
  livros.append([titulo, autor, ano])
with open('livros.csv', 'w', newline='') as arq:
  escrita = csv.writer(arq)
  escrita.writerows(livros)
print('informacao incluida com sucesso')