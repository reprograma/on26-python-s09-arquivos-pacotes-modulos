from data_util import calculo_idade, ano_bissexto, formatar_data

#pedir ao user que informe sua data de nascimento no formato "dd/mm/aaaa" 

data_nascimento_user =input(f"Insira sua data de nascimento no formato 'dd/mm/aaaa': \n")

#calcular a idade usando a função de dentro do módulo que criamos.

idade = calculo_idade.calcular_idade(data_nascimento_user)

print(f"Sua idade é: {idade} anos")


#verificar se o ano atual é bissexto usando a função do módulo ano_bissexto

ano_atual = int(input("Digite o ano atual para verificar se é bissexto: "))
if ano_bissexto.eh_ano_bissexto(ano_atual):
    print(f"{ano_atual} é um ano bissexto.")
else:
    print(f"{ano_atual} não é um ano bissexto.")


#solicitar uma data do usuário e formatá-la usando a função do módulo formatar_data

data_input = input("Digite uma data (dd/mm/aaaa), qualquer, para usarmos outra formatação: ")
data_formatada = formatar_data.formatar_data(data_input)
print(f"A data formatada é: {data_formatada}")

