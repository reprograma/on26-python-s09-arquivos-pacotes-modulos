from pacote_nanda import bissexto
ano_querido = input("Digite o ano que você quer saber: ")

if bissexto(ano_querido):
    ano_yes = print("É um ano bissexto")
else:
    ano_not = print("Não é ano bissexto")
