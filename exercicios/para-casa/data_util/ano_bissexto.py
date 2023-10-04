def ano_bissexto(ano):
    if (ano % 4 ==0 and ano %100 != 0):
        print('O ano é bissexto')
        return True

    else:
        print('O ano não é bissexto')
        return False

        