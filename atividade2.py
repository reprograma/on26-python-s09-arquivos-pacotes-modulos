from data_util import ano_bissexto
from data_util import calculo_idade

ano = int(input('informe o ano que deseja verificar: '))
print(ano_bissexto.verificar_bi(ano))

def verificar_bi(ano):
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
         return True
    else:
        return False