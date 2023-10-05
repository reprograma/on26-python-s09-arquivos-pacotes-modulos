import csv

with open("./doc_leitura.txt", "r") as arq: 
    conteudo_doc_leitura = arq.readline() #aqui ele leu, pega o arq e lê a primeira linha dele
    print(conteudo_doc_leitura)