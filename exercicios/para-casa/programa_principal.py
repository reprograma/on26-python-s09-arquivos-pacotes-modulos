from data_util import calculo_idade

data_nascimento = "01/01/1980"
idade = calculo_idade.calcular_idade(data_nascimento)
print(f"A idade da pessoa é de {idade} anos.")


from data_util import formatar_data

data = "01/01/1980"
data_formatada = formatar_data.formatar_data(data)
print(data_formatada)


from data_util import ano_bissexto

ano = 2024
eh_bissexto = ano_bissexto.eh_ano_bissexto(ano)
print(f"O ano {ano} é bissexto? {eh_bissexto}")