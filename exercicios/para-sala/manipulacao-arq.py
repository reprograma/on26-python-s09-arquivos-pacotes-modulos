
# 'r' = read

with open('./dados.txt', 'r') as arquivos:
    conteudo = arquivos.read()
    print(conteudo)


# retornando o conteudo e as linhas como uma lista
with open('./dados.txt', 'r') as arquivos:
    linhas = arquivos.readlines()
    print(linhas)

# 'w' = write

with open('./dados-write.txt', 'w') as arquivos:
    arquivos.write("fim de linha")
    