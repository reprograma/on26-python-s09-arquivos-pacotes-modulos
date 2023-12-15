def ano_bissxto(ano):
    if(ano % 4 == 0 and ano %100 != 0) or (ano %400 == 0):
        return True
    else:
        return False
    

# Vê se o ano é bissexto pela conta. Se o ano for dividido por 4 e não por 100 ou por 400, dirá se é bissexto ou não(verdadeiro ou falso)