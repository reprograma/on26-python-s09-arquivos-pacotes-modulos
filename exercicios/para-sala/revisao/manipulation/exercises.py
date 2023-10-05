import csv

books = []
# Recuperar os dados do arquivo livros.csv
with open('books.csv', 'r') as file:
    read = csv.reader(line)
    for line in read:
        title, author, year = line
        books.append([title, author, year])

# input das informações
while True:
    title = input("Enter the title of the book or the word exit")
    if title.lower() == 'exit':
        break
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    books.append([title, author, year])

# Salvar os dados que ficou em lista livros = []
with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(books)

if title.lower() != 'exit':
    print('Information added success fully')