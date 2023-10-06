from datetime import datetime

def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year
    if (data_atual.month, data_atual.day) < (data_atual.month, data_atual.day):
      return idade - 1
    else:
       return idade




