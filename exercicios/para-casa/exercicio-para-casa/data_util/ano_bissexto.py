def eh_ano_bissexto(ano):
    # Verifica se um ano é bissexto de acordo com as regras:
    # - É divisível por 4, mas não por 100, a menos que seja divisível por 400.
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True  # Retorna True se o ano é bissexto.
    else:
        return False  # Retorna False se o ano não é bissexto.
