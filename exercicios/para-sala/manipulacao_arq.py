import csv

#with open('./dados.txt', 'r') as arq: # as tem funcionalidade de 
    #conteudo = arq.read() #'r'=modo arquivo leitura/ler
    #print(f'{conteudo} - Aluna Reprograma')
   # linha = arq.readlines() #uso isso(readline) para ler uma linha expecifica e se eu quiser todas as linhas faço isso no plural(readlines)
   # print(linha)
    #print(linha[2])


with open('./dados1.txt', 'w') as arquivo:   #w= arquivo modo de escrita write/para criar um arquivo novo dados1.txt
    arquivo.write("fim de de carreira ahhahah ")


dados =[["Nome", "Idade",],["Aline", 30], ["Bob",25]]

with open('pessoas.csv', 'w', newline='') as arq_csv:
    escritor_csv = csv.writer(arq_csv)
    escritor_csv.writerows(dados)

with open('pessoas.csv', 'r', newline='') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)

import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)   

