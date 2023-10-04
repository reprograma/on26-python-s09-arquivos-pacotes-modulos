from datetime import date

data_informada = input('informe a data desejada no formato aaaa/mm/dd: ')
data_formatada = date.strftime(data_informada, '%d/%m%Y')
print(data_formatada)

from datetime import date, time, datetime

def calcular_idade(data_nascimento):
    idade = (date.today()) - data_nascimento
    return(idade)

data = input('informe sua data de nascimento: ')
data_nascimento = date.strftime(data, '%d/%m/%Y')
data_atual = date.today()
calcular_idade = (data_atual - data_nascimento)
print(calcular_idade)