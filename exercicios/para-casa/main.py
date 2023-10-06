from datetime import datetime
from data_util import ano_bissexto, calculo_idade, formatar_data

data_nascimento = input("\n Insira uma data no formato dd/mm/aaaa: ")
idade = calculo_idade.calcular_idade(data_nascimento)

ano_atual = int(input("\n Insira um ano para verificar se é bissexto "))
if ano_bissexto.eh_ano_bissexto(ano_atual):
    print(f"\n {ano_atual} é um ano bissexto")

else:
    print(f"\n {ano_atual} não é ano bissexto")



data_input = input("\n Insira uma data (dd/mm/aa): ")
data_formatada = formatar_data.formatar_data(data_input)
print(f"\n A data formatada é {data_formatada}")
