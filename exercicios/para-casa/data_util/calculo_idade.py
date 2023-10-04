# Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa
from datetime import date, time, datetime

def calcular_idade(data_nascimento):
    idade = (date.today()) - data_nascimento
    return(idade)

data = input('Informe sua data de nascimento: ')
data_nascimento = date.strftime(data, "%d/%m/%Y")
data_atual = date.today()
calcular_idade = (data_atual - data_nascimento)
print(calcular_idade)

# dia_nascimento = int(input('Informe seu dia de nascimento: '))
# mes_nascimento = int(input('Informe seu mês de nascimento: '))
# ano_nasicmento = int(input('Informe seu ano de nascimento: '))
