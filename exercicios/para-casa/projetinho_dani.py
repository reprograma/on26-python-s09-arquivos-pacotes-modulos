from data_util import ano_bissexto, calculo_idade, formatar_data


data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa):')
idade = calculo_idade.calcular_idade(data_nascimento)
print(f"Sua idade é {idade} anos!")


ano_atual = int(input("Digite um ano para verificação de ano bissexto: "))
if ano_bissexto.eh_ano_bissexto(ano_atual):
     print(f'{ano_atual} é um ano bissexto')
else:
     print(f'{ano_atual} não é um ano bissexto')


data_requerida = input("Digite uma data no formato (dd/mm/aaaa): ")  
data_formatada = formatar_data.data_formatada(data_requerida)
print(f"A data formatada é {data_formatada}") 






