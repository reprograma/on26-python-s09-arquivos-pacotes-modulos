from datetime import datetime



def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%y")
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - \
        ((data_atual.day, data_atual.month) < \
         (data_nascimento.day, data_nascimento.month))
    return idade

