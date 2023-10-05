import csv

with open("./nome_pessoas.csv", "r") as arq_pessoas:
    leitor_pessoas = csv.reader(arq_pessoas, delimiter=",")
    linhas = 0 
    for dados_colunas in leitor_pessoas:
        if linhas == 0:
            print(f"Dados: {dados_colunas}.")
            linhas +=1
        else: 
            print(f"\tNome Completo: {dados_colunas[0]}, \n\tIdade: {dados_colunas[1]} anos.")
            linhas +=1

        
        