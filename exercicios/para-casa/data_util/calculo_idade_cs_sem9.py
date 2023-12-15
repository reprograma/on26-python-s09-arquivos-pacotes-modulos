
from datetime import datetime

def calculo_idade(data_nasc):
    data_nasc = datetime.strptime(data_nasc, "%d/%m/%y")
    data_atual = datetime.now()
    idade = data_atual.year - data_nasc.year - ((data_atual.day, data_atual.month) < (data_nasc.day, data_nasc.month))
    return idade


# Faz o cálculo da idade comparando dia, mês e ano(data de hoje com a data do nascimento).