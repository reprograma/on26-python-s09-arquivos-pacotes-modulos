from data_util import ano_bissexto_cs_sem9, calculo_idade_cs_sem9, formatar_data_cs_sem9

data_nascimento = input(" Digite sua data de nascimento: ")
idade = calculo_idade_cs_sem9.calculo_idade(data_nascimento)
print (f" Sua idade é {idade}. ")

ano_atual = int(input ("Didite um ano para saber se é bissexto: "))
if ano_bissexto_cs_sem9.ano_bissxto(ano_atual):
    print(f"{ano_atual} é um ano bissexto. ")
else:
    print(f"{ano_atual} não é um ano bissexto. ")


data_input = input("Digite uma data: . ")
data_formatada = formatar_data_cs_sem9.formatar_data(data_input)
print(f" A data formatada é {data_formatada}")