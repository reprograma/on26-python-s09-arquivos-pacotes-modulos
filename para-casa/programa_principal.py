from data_util import formatar_data
from data_util import ano_bissexto
from data_util import calculo_idade
from datetime import date

dia_nasc = int (input("Digite o dia que você nasceu: "))
mes_nasc = int (input("Digite o mês que você nasceu: "))
ano_nasc = int (input("Digite o ano que você nasceu: "))

print (f"Sua data de nascimento é: {dia_nasc}/{mes_nasc}/{ano_nasc}")
idade = calculo_idade.calcular_idade(ano_nasc)
print (f"Sua idade atual é: {idade} anos ")

ano_atual = int (input("Digite o ano atual: "))
ano_bi = ano_bissexto.sim_ano_bissexto(ano_atual)
print (f"O ano {ano_atual} é bissexto? {ano_bi} ")

data_hoje = input ("Digite uma data: dd/mm/aaaa: ")
data_formatada = formatar_data.formatar_data(data_hoje)
print (data_formatada)

    
    
    