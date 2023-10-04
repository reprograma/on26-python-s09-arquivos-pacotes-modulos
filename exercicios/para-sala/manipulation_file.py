import csv

#with open ('./datas.txt', 'r') as file: #vai ler o arquivo
    #content = file.read() #depois que ele lê a primeira linha ele exclui as posteriores
    #print(f'{content} -Goku')
    #line = file.readline() #ler um linha, no sigurla sempre uma linha
    #print (line)
    #lines = file.readlines() #ler varias linhas, imprime todas as linhas
    #print (lines)
    #print(lines[1]) #add a posição da linha buscada

#escrita do arquivo, pode adcionar criar um novo arquivo basta altera o nome ./endereço, ex=./dados1.txt
#with open('./datas.txt', 'w') as file: 
    #manda para o aqrquivo
    #file.write('Oi eu sou um  Goku') 
#datas1 = [['nome', 'idade'], ['Mirley', 26], ['Beyonce', 42]]
#with open('people.csv', 'w', newline='') as file_csv: #se n tiver um arquivo do fomato será criado um
    #escritor_csv = csv.writer(file_csv) #escreve dentro do arquivo
    #escritor_csv.writerows(datas1)

#with open('people.csv', 'r') as file: #um loop que irá ler todas as linhas
    #leitor_csv = csv.reader(file_csv)
    #for line in leitor_csv:
        #print(line)

import json
#maneira de guardar os dados, principalmente em API no back and e front end
datas = {'nome':'Delise', 'idade':25, 'cidade':'floripa'}
with open('datas.json', 'w') as file_json:
    json.dump(datas, file_json)
#dump joga os dados da lista dentro do arquivo json

with open('datas.json', 'r') as file_json:
    datas= json.load(datas, file_json)
    print(datas)