# Contém uma função verificador_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False

import datetime

def verificar_bissexto(ano):
    verificador = ano % 4
    if verificador == 0:
        return True
    else:
        return False