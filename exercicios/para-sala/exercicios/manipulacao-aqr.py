
# with open ('./dados.txt', 'r') as arq: #read
    # content = arq.read() 
    # print(f'{content} - Professora')
#   linha = arq.readlines()
#    print(linha)
#   print(linha[1])

# with open('./dados.txt', 'w') as arq:
#    content = arq.write("fim de linha")


#import csv

#dados = [['nome', 'idade'], ['alice', 30], ['bob', 25]]
#with open('pessoas.csv', 'w', newline= '') as arq_csv:
 #  escritor_csv = csv.writer(arq_csv)
  # escritor_csv.writerows(dados)

# import json

#dados = {'nome': "Alice", 'idade': 30, 'cidade': 'Exemploville'}

with open ('dados.json', 'w') as arq_json:
   json.dump(dados, arq_json)

with open ('dados.json', 'w') as arq_json:
   json.load(dados, aqr_json)
   print(dados)
