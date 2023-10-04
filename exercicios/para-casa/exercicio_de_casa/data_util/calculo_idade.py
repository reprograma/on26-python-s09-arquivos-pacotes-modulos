import datetime

current_date = datetime.date.today()
data_nascimento = datetime.date

def calcular_idade(data_nascimento, current_date):
    if (current_date.month, current_date.day) < (data_nascimento.month, data_nascimento.day):
        return current_date.year - data_nascimento.year - 1
    else:
        return current_date.year - data_nascimento.year

# # # atribuindo valores para testar
# data_nascimento1 = datetime.date(1995, 4, 6)
# data_nascimento2 = datetime.date(1995, 12, 25)

# # # rodando a função para testar 
# calcular_idade(data_nascimento1, current_date)
# calcular_idade(data_nascimento2, current_date)

