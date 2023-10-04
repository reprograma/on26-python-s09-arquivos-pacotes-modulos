from datetime import datetime 

def eh_ano_bissexto(ano):
    
    #ano = int(input('Ano: '))
 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
  return True
 else:
  return False