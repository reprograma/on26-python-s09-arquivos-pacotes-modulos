#with open ('./exercio1.txt', 'r') as file: #vai ler o arquivo
    #content = file.read() #depois que ele lê a primeira linha ele exclui as posteriores
    #print(f'{content} - Pathria')

#import json
#datas = {'S':'Entropia', 
        #'T': "temperatura",
        #'ni':'Potencial Quimico'
        #}
#with open('datas.json', 'w') as file_json:
    #json.dump(datas, file_json)
#with open('datas.json', 'r') as file_json:
    #datas_lidos= json.load(file_json)
    #print(datas)

import csv
with open('alunos.csv', 'r') as file: #um loop que irá ler todas as linhas
    leitor_csv = csv.reader(file)
    total_alunos= 0
    total_notas = 0
    for line in leitor_csv:
        nome, idade, nota = line
        nota = float(nota)
        total_notas = total_notas + nota
        total_alunos = total_alunos + 1
    
    if total_alunos>0:
        media=total_notas/total_alunos
        print(f'a média das notas é {media}')
    else:
        print('Inválido')