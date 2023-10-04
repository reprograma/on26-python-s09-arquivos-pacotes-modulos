from data_util import ano_bissexto
from data_util import formatar_data
from data_util import calculo_idade

ano = int(input('Informe o ano que deseja verificar: '))
print(ano_bissexto.verificar_bi(ano))

data=input("Digite a data de nascimento:")
print(formatar_data.data_formatar())