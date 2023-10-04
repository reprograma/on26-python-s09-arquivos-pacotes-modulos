#Contém uma função eh_ano_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False
# Exercício feito em grupo

def eh_ano_bissexto(ano):
    # ano = int(input('Informe o ano para saber se é ou não bissexto: {}'))
    if (ano % 4 == 0) and (ano % 100 != 0) or (400 == 0):
        return True
    else:
        return False
        
