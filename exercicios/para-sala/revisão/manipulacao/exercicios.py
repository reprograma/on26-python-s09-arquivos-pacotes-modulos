import csv
livros = []

while True:
    titulo = input("Digite o nome do livro ou palvra sair=")
    if titulo.lower() == 'sair':
        print('Saindo do programa...')
        break
    autor=input("Digite o nome do autor=")
    ano= input('Digite o ano da publiacação=')
    livros.append([titulo, autor, ano])
with open('livros.csv', 'w') as file:
    escrita=csv.writer(file)
    escrita.writerow(livros)

if titulo.lower !='sair':
    print('informação incluida com sucesso')

