# **Exercício 1: Leitura de um arquivo TXT**

# Crie um arquivo de texto chamado "dados.txt" com algumas linhas de texto. Escreva um programa em Python que leia o conteúdo do arquivo e exiba-o na tela.

   
with open('dado.txt', 'r') as arq: 
    conteudo = arq.read()
    print(conteudo)