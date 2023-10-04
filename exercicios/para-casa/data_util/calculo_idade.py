# Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa
import datetime

def calcular_idade(data_nascimento):
    data_hoje = datetime.datetime.now()
    idade = data_hoje.year - data_nascimento.year
    if data_hoje.month <= data_nascimento.month:
        if data_hoje.day < data_nascimento.day:
            idade -= 1
    return idade