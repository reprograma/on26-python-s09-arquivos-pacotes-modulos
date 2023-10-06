import csv

#with open('./dados.txt', 'r') as arq:
    #conteudo = arq.read()
    #print(f'{conteudo}.Professora')
    #linha = arq.readlines()
    #print(linha[0])

"""with open('./dados1.txt', 'w') as arq2:
    arq2.write("Fim de linha")"""

''''dados = [['nome', 'idade'], ['Dani', 38], ['Gabriel', 17], ['Ricardo', 36], ['Braz', 61]]

with open('pessoas.csv', 'w', newline='') as arq_csv:
    escritor_csv = csv.writer(arq_csv)
    escritor_csv.writerow(dados)

with open('pessoas.csv', 'r') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)
'''
import json

dados = {'nome': 'Daniele', 'idade': 38, 'cidade': 'Valenca'}
with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

    
curso = {'Curso': 'Matematica','Instituicao': 'Ifba'}
with open('curso.json', 'w') as arq_json:
    json.dump(curso, arq_json)

with open('dados.json', 'r') as arquivo_json:
   dados = json.load(arquivo_json)
   print(dados)
