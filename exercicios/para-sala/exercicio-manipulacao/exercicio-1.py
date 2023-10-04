# Abre o arquivo 'dados.txt' no modo leitura ('r').
with open('dados.txt', 'r') as arq:
    conteudo = arq.read()  # Lê todo o conteúdo do arquivo e armazena em 'conteudo'.
    print(conteudo)  # Imprime o conteúdo lido do arquivo.
