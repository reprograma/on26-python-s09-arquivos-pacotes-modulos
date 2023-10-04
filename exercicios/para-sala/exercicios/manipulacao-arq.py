#import csv
import json


"""with open('./dados.txt', 'r') as arq:
    #conteudo = arquivos.read()
    #print(f'{conteudo} - Professora')
    linhas = arquivos.readlines()
    print(linhas[1])
    """
    
"""with open('./dados1.txt', 'w') as arquivo:
        arquivo.write ("fim de linha")
        """
        
        
"""dados =[['nome', 'idade'], ['Alice', 30], ['Bob', 25]]         
with open('pessoas.csv', 'w', newline='') as arq_csv:
    escritor_csv = csv.writer(arq_csv)
    escritor_csv.writerows(dados)
    """
    
"""import csv

with open('pessoas.csv', 'r', newline='') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)
"""
        

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}

"""with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)  # dump( cria e joga os arquivos dentro/ json guarda dados em forma de objetos/
    # api elo entre duas coisas no programa, e tem um padrão(consumir json)   
        """


with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)