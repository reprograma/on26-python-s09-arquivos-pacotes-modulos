import csv
import json

# Abre o arquivo "dados.txt" no modo leitura ('r').
with open ('./dados.txt', 'r') as arquivos:
    conteudo = arquivos.read()  # Lê o conteúdo completo do arquivo e armazena em 'conteudo'.
    print(f'{conteudo} - Me')  # Exibe o conteúdo e a string " - Me".
    linhas = arquivos.readlines()  # Lê todas as linhas do arquivo e armazena em 'linhas'.
    print(linhas[1])  # Imprime a segunda linha do arquivo.
    linha = arquivos.readline()  # Lê a próxima linha do arquivo, mas não faz nada com ela.
    print(linha)  # Imprime a linha lida acima (provavelmente estará vazia).

# Abre o arquivo "dados1.txt" no modo escrita ('w') e escreve "fim de linha".
with open('./dados1.txt', 'w') as arquivo:
    arquivo.write("fim de linha")

# Cria uma lista de dados chamada 'dados'.
dados = [['nome', 'Idade'], ['alice', 30], ['bob', 25]]

# Abre o arquivo "pessoas.csv" no modo escrita ('w') usando a biblioteca csv.
with open('pessoas.csv', 'w', newline='') as arq_csv:
    escritor_csv = csv.writer(arq_csv)
    escritor_csv.writerows(dados)  # Escreve os dados no arquivo CSV.

# Abre o arquivo "pessoas.csv" no modo leitura ('r') usando a biblioteca csv.
with open('pessoas.csv', 'r', newline='') as arq:
    leitor_csv = csv.reader(arq)
    for linha in leitor_csv:
        print(linha)  # Lê e imprime cada linha do arquivo CSV.

# Cria um dicionário de dados chamado 'dados'.
dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}

# Abre o arquivo "dados.json" no modo escrita ('w') e escreve o dicionário em formato JSON.
with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

# Abre o arquivo "dados.json" no modo leitura ('r') e carrega o dicionário JSON de volta.
with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)  # Imprime o dicionário JSON carregado.
