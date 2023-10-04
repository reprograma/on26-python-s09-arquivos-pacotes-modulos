import sys
sys.path.append('C:\\Users\\nargy\\estudos\\semana-9\\on26-python-s09-arquivos-pacotes-modulos\\exercicios\\para-casa\\pacote_nanda')

from pacote_nanda import modulo1

ano_nasceu = int(input("Qual o seu ano de nascimento?: "))
ano_atual = int(input("Em que ano você está?: "))

print(f"Sua data de nascimento é {modulo1.subtracao} anos")