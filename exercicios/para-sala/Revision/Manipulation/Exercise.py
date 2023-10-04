import csv

books = []

#Para continuar salvando as informações passadas

with open("books.csv", "r") as arq:
    writing = csv.reader(arq)
    for line in writing:
        title, author, year = line
        books.append([title, author, year])

while True:
    title = input("Enter title of book or exit")
    if title.lower() == "exit":
        print("Leaving of program")
        break
    author = input("Enter name author:\n")
    year = input("Enter year of publish:\n")
    books.append([title, author, year])
    
with open("books.csv", "w", newline="") as arq:
    writing = csv.writer(arq)
    writing.writerows(books)

if title.lower() != "Exit":
    print("Information added successfully ")