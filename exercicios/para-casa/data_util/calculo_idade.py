# Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa
from datetime import datetime, timedelta

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje - data_nascimento
    return idade

dia_nascimento = int(input('Informe seu dia de nascimento: '))
mes_nascimento = int(input('Informe seu mês de nascimento: '))
ano_nasicmento = int(input('Informe seu ano de nascimento: '))
data_nascimento = datetime(day=dia_nascimento, month=mes_nascimento, year=ano_nasicmento)
idade = calcular_idade(data_nascimento)
print(idade) # Resultado em dias e horas. Como converter para anos?