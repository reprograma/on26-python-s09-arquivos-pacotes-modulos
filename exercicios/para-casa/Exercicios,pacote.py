import datetime

def calcular_idade(data_nascimento):
    data_nascimento = datetime.datetime.strptime(data_nascimento, 07/06/1990)
    hoje = datetime.datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def eh_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
import datetime

def formatar_data(data):
    data_obj = datetime.datetime.strptime(data, "%d/%m/%Y")
    data_formatada = data_obj.strftime("%Y-%m-%d")
    return data_formatada
from data_util import calculo_idade, ano_bissexto, formatar_data

data_nascimento = input("Digite sua data de nascimento (07/06/1990): ")

idade = calculo_idade.calcular_idade(data_nascimento)
print(f"Sua idade é: {idade} anos")

# Verificar se o ano atual é bissexto
ano_atual = datetime.date.today().year
if ano_bissexto.eh_ano_bissexto(ano_atual):
    print(f"{ano_atual} é um ano bissexto.")
else:
    print(f"{ano_atual} não é um ano bissexto.")

# Solicitar uma data ao usuário e formatá-la
data = input("Digite uma data (dd/mm/aaaa): ")
data_formatada = formatar_data.formatar_data(data)
print(f"A data formatada é: {data_formatada}")
