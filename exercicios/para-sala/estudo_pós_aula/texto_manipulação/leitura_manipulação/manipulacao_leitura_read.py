import csv
        
with open("./doc_leitura.txt", "r") as arq: 
    conteudo_doc_leitura = arq.read() #aqui ele falou assim "Pega o arq(o nome que demos para o arquivo lá em cima.) e ler"
    print(conteudo_doc_leitura)