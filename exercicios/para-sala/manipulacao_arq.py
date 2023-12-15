import csv
import json

#with open("./dados.txt", "r") as arq:
    #conteudo = arq.read()
    #print(f"{conteudo} - Aluna")
#    linha = arq.readlines()  #se colocar readline (singular) conta as letras
    #print(linha)
#    print(linha[2])

#with open("./dados1.txt", 'w') as arquivo:
#    arquivo.write("fim de linha")

#dados = [["nome", "idade"], ["alice", 30], ["bob", 25]]     #CSV- CRIA TABELAS

#with open("pessoas.csv", "w", newline="") as arq_csv:
#   escritor_csv = csv = csv.writer(arq_csv)
#    escritor_csv.writerows(dados)

#with open("pessoas.csv", "r", newline="") as arq:
#    leitor_csv = csv.reader(arq)
#    for linha in leitor_csv:
#        print(linha)


#dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}   
# # JSON CRIA ARQUIVO EM FORMA DE DICIONARIO 

#with open('dados.json', 'w') as arquivo_json:
#    json.dump(dados, arquivo_json)

with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)