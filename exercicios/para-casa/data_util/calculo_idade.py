# data_util/calculo_idade.py
import datetime

def calcular_idade(data_nascimento):
    data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    data_atual = datetime.date.today()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade
