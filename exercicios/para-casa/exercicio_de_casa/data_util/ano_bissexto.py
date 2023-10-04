def eh_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 != 0:
            return True
        else:
            return False
    else:
        return False

# # testando o código
# ano1 = 2000
# ano2 = 2016
# ano3 = 2003

# resultado1 = eh_ano_bissexto(ano1)
# resultado2 = eh_ano_bissexto(ano2)
# resultado3 = eh_ano_bissexto(ano3)

# print(resultado1)
# print(resultado2)
# print(resultado3)