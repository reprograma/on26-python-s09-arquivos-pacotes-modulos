import csv

print("Coloque aqui as informações do livro que deseja adicionar.")

nome_livro_user = input("Nome do livro: \n")
nome_autor_user = input("Nome do autor do livro: \n")
data_lancamento = input("Data de lançamento do livro: \n")

cabecalho = ["Nome do livro", " autor do livro", " data de lançamento do livro"]

with open("./livros_ex4.csv", "r") as arq_cabecalho:
    leitor_csv = csv.reader(arq_cabecalho)
    
    
    print("Cabeçalho do arquivo CSV:")
    print(",".join(cabecalho))

tab_livro = [nome_livro_user, nome_autor_user, data_lancamento]

with open("./livros_ex4.csv", "a") as arq_livros:
    info_livros = csv.writer(arq_livros, delimiter=",")
    
    if arq_livros.tell() == 0:
        info_livros.writerow(cabecalho)
    
    info_livros.writerow(tab_livro)
