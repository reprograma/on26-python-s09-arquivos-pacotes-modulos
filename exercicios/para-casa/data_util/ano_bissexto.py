ano = input('Digite o ano: ')

def eh_ano_bissexto(ano):
    if (ano % 4) == 0:
        if (ano % 100) == 0:
            if (ano % 400) == 0:
                return True
            else:
                return False
        else:
            return True
            print(f'o {ano} é bissexto')
    else:
        return False