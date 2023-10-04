import csv  #biblioteca csv

#**Abrindo arquivos**
"""with open('./dados.txt','r') as arq: # ler arqivos emm outro documento
    #conteudo = arq.read()
    #print(conteudo)
    linhas = arq.readlines() # executa as linhas como lista - readline no sincular imprime apenas uma linha
    print(linhas)
    print(linhas[2]) # printar o objeto na lista

with open("./dados1.txt", "w") as arquive:
    arquive.write("Fim de linha")"""

# **Criando e escrevendo um arquivo**
"""dados = [['nome', 'idade'], ['alice', '30'], ['bob', 25]]

with open('pessoas.csv', 'w', newline='') as arq_csv: #arquivo pessoa não exite o sistema cria
    escritor_csv = csv.writer(arq_csv)
    escritor_csv.writerows(dados)  #escrever linha por linha, num arquivo excel

with open('pessoas.csv', 'r') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)"""

import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

with open ('dados.json', 'r') as arquivo_json:
    dados  = json.load(arquivo_json)
    print(dados)
