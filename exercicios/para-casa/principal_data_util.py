from data_util import calculo_idade
from data_util import ano_bissexto
from data_util import formatar_data



idade_pessoa = calculo_idade.calcular_idade(2023,1990)
print('Você tem:',idade_pessoa, 'anos')
# print(f'Você tem: {idade_pessoa} anos')

info_bissexto = ano_bissexto.ano_bissexto(1990)
print(info_bissexto)

converte_data = formatar_data.formatar_data(2)
print(converte_data)





#feito em grupo