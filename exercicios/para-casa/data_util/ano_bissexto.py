from datetime import datetime
def eh_ano_bissexto(ano):
  if ano % 4 == 0:
    return False
  else:
    return True