from data_util import calculo_idade, ano_bissexto, formatar_data

# Inserir data de nascimento
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Cálculo da idade com base na informação do usuário
idade = calculo_idade.calcular_idade(data_nascimento)
print(f"Sua idade é: {idade} anos")

# Verificando se o ano aual é bissexto
ano_atual = int(input("Digite o ano atual: "))
if ano_bissexto.eh_ano_bissexto(ano_atual):
    print(f"{ano_atual} é um ano bissexto.")
else:
    print(f"{ano_atual} não é um ano bissexto.")

# Solicitando data, alterando formato para data_time
data = input("Digite uma data (dd/mm/aaaa): ")
data_formatada = formatar_data.formatar_data(data)
print(f"A data formatada é: {data_formatada}")

