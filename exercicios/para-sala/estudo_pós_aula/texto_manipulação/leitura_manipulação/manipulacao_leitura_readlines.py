import csv

with open("./doc_leitura.txt", "r") as arq:
    conteudo_doc_leitura = arq.readlines() #aqui ele leu, abre para mim em forma de LISTA esse arquivo. 
    print(conteudo_doc_leitura)
    print("************")
    #se quisermos colocar uma linha específica do doc, usamos o índice dele
    print(conteudo_doc_leitura[2])
    

