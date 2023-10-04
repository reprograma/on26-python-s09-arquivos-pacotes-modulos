

#with open('./dados.txt', 'r') as arq: #'r' = read, está chamando o arquivo para ler
    #conteudo = arq.read() #executa o conteusodo
    #print(conteudo)
    #print(f'{conteudo} - Aluna')
    #linhas = arq.readlines() #executa todas as linhas como lista
    #print(linhas)
    #readline executa apenas uma lista
    #linha = arq.readline()
   # print(linha)

    #ex = ('gg', 'ff', 'rr')
    #print(ex[2])

#with open('.dados1.txt', 'w') as arquivo: #'w' write = escrever no arquivo, caso não tenha um arquivo com esse nome ele cria
#    arquivo.write('Fim da linha')

#import csv #biblioteca

# dados = [['nome', 'idade'], ['Alice', 11], ['Andre', 4]]

# with open('pessoas.csv', 'w', newline='') as arq_csv:
#     escritor_csv = csv.writer(arq_csv)
#     escritor_csv.writerows(dados) # writerows = para escrever linha por linha 

# with open('pessoas.csv', 'r') as arq: # aqui é para printar linha por linha
#       leitor_csv = csv.reader(arq)
#       for linha in leitor_csv:
#            print(linha)

# with open ('pessoas.csv', 'r', newline='') as arq:
#      leitor_csv = csv.reader(arq)
#      for linha in leitor_csv:
#           print(linha)

import json #biblioteca

# dados = {'nome': 'Alice', 'idade': '11', 'cidade':  'Exemploville'} #esta escrevendo

# with open('dados.json', 'w') as arquivo_json:
#     json.dump(dados, arquivo_json)

# with open('dados.json', 'r') as arquivo_json: #esta lendo
#     dados = json.load(arquivo_json)
#     print(dados)
 
    
