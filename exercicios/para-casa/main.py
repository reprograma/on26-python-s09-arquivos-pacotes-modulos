#meu código:
#Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.
# from data_util import calculo_idade, formatar_data, ano_bissexto

# data_nascimento = int(input("Digite a data do seu nascimento, no formato dd/mm/aaaa: "))
# idade = data_util.calculo_idade(data_nascimento)
# print("Sua idade é ", {idade})

#Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`.
# ano = input("Digite um ano: ")

#Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd".
# data = input("Digite uma data no formato dd/mm/aaaa: ")
# print(data)

#código da professora:
from data_util import ano_bissexto, calculo_idade, formatar_data
data_nascimento = input("digite sua data (dd/mm/aaaa) de nascimento:")
idade = calculo_idade.calcular_idade(data_nascimento)
print(f"{idade}")

ano_atual = int(input("digite um ano para verificar se  é bissexto: "))
if ano_bissexto.eh_ano_bissexto(ano_atual):
    print(f"{ano_atual} é um ano bissexto.")
else:
        print(f"{ano_atual} não é um ano bissexto.")

data_input = input("digite uma data (dd/mm/aaaa): ")
data_formatada = formatar_data.formatar_data(data_input)
print(f"A data formatada é {data_formatada}")