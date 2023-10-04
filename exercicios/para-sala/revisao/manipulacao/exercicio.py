import csv  # Importa o módulo CSV para lidar com arquivos CSV

livros = []  # Inicializa uma lista vazia chamada 'livros' para armazenar informações dos livros

# Abre o arquivo 'livros.csv' no modo de leitura ('r') usando o contexto 'with'
with open('livros.csv', 'r') as arq:
    leitor = csv.reader(arq)  # Cria um leitor CSV para ler o arquivo
    for linha in leitor:  # Loop para percorrer cada linha do arquivo CSV
        titulo, autor, ano = linha  # Desempacota os valores da linha em título, autor e ano
        livros.append([titulo, autor, ano])  # Adiciona os dados à lista 'livros'

# Entra em um loop infinito para permitir ao usuário adicionar mais livros ou sair do programa
while True:
    titulo = input("Digite o título do livro ou a palavra 'Sair': ")
    if titulo.lower() == "sair":  # Verifica se o usuário quer sair do programa
        print("Saindo do programa...")
        break  # Sai do loop infinito se o usuário digitar 'Sair'
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")
    livros.append((titulo, autor, ano))  # Adiciona os dados do novo livro à lista 'livros'

# Abre o arquivo 'livros.csv' no modo de escrita ('w') usando o contexto 'with'
with open('livros.csv', 'w', newline='') as arq:
    escrita = csv.writer(arq)  # Cria um escritor CSV para escrever no arquivo
    escrita.writerows(livros)  # Escreve os dados da lista 'livros' de volta ao arquivo CSV

if titulo.lower() != 'sair':
    print('Informação incluída com sucesso.')  # Exibe uma mensagem de sucesso se não tiver saído do programa
