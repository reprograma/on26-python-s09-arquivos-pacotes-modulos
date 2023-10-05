from datetime import datetime
from data_util import ano_bissexto, calculo_idade, formatar_data

data = input("\n Insira uma data no formato dd/mm/aaaa: ")
data_formatada = formatar_data.formatar_data(data)
ano_nascimento = int(data.split("/")[-1])

idade_calculada = calculo_idade.calcular_idade(data)

if ano_bissexto.eh_ano_bissexto(int(data.split("/")[-1])):
    print("\n Ano não bissexto")
else:
    print("\n Ano bissexto")

print(f"\n {idade_calculada} anos de idade")