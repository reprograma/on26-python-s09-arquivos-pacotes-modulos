import datetime

from data_util import ano_bissexto, formatar_data, calculo_idade

# criando variáveis neste ambiente com input de usuário
print("Insira uma data no formato dd/mm/aaaa")
input_usuario_dia = int(input('dd ')) 
input_usuario_mes = int(input('mm '))
input_usuario_ano = int(input('aaaa '))

# criando variáveis necessárias
current_date = datetime.date.today()
data_nascimento = datetime.date(input_usuario_ano, input_usuario_mes, input_usuario_dia)

# rodando as funções
idade = calculo_idade.calcular_idade(data_nascimento, current_date)
print(f'A idade é {idade}')

eh_bissexto = ano_bissexto.eh_ano_bissexto(input_usuario_ano)
if eh_bissexto:
    print(f'O ano informado {input_usuario_ano} é bissexto')
else:
    print(f'O ano informado {input_usuario_ano} não é bissexto')

data_formatada = formatar_data.formatar_data_tentativa2(input_usuario_dia, input_usuario_mes, input_usuario_ano)
print(f'Data formatada:{data_formatada}')



