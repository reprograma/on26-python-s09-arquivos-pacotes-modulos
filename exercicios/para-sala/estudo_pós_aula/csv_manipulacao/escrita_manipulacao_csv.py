import csv

dados = [['Nome', 'Idade'], ['Alice', 30], ['Bob', 25]]

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)

#Outro jeito 

dados2 = [['Nome', 'Idade'], ['Thaysa', 20], ['Luana', 25]]

        #se o nome do arquivo não existir, python irá criar ele. 
with open('dados2.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados2)