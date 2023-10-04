# Exercicio para casa Cris Pereira - semana 09 - curso Python - prof Daviny
import datetime
from data_util import ano_bissexto, calculo_idade, formatar_data

print("** Programa Data Útil **")
data_usuario = input("Digite uma data no formato dd/mm/aa: ")
data_convertida = datetime.datetime.strptime(data_usuario, "%d/%m/%Y")
verificador_bissexto = ano_bissexto.verificar_bissexto(data_convertida.year)
idade = calculo_idade.calcular_idade(data_convertida)
data_formatada = formatar_data.formatar_data(data_convertida)

print(f"A idade atual de quem nasceu em {data_usuario} é {idade} anos.")

if verificador_bissexto == True:
    print(f"O ano de nascimento é bissexto.")
else:
    print(f"O ano de nascimento não é bissexto.")

print(f"A data de nascimento formatada em aaaa-mm-dd é: {data_formatada}")
