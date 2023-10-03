#Essa é a minha página principal
from data_util import calculo_idade #fazendo a importação
from data_util import ano_bissexto
from data_util import formatar_data

#calculo_idade.projeto_feliz() #chamando o módulo

# dia_nascimento = int(input('Digite a dia de nascimento: '))
# mes_nascimento = int(input('Digite o mês de nascimento: '))
# ano_nascimento = int(input('Digite o ano de nascimento: '))

# print('Sua data de aniversário é: ', dia_nascimento, '/', mes_nascimento,'/',ano_nascimento)

idade_pessoa = calculo_idade.calcular_idade(2023,1995)
print('Você tem:',idade_pessoa, 'anos')
# print(f'Você tem: {idade_pessoa} anos')

info_bissexto = ano_bissexto.eh_ano_bissexto(1995)
print(info_bissexto)

convert_data = formatar_data.formatar_data(2)
print(convert_data)

