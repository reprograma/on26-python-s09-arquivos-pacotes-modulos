#def verificar_bi(ano):
   # return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
#ano= int(input("Digite o ano que deseja verificar="))
  
    
#if verificar_bi(ano):
   # print(f'o ano de {ano} é bisexto')
#else:
    #print(f'o ano de {ano} não é bisexto')
#daqui pra cima roda

def verificar_bi(ano):
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
         return True
    else:
        return False
   