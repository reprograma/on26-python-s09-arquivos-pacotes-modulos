import datetime

# # primeira tentativa, depois descartada:
# def formatar_data_tentativa1(input_usuario_dia, input_usuario_mes, input_usuario_ano):
#     while True:
#         input_usuario_dia = int(input("Insira uma data começando pelo dia: "))
#         if input_usuario_dia < 1 or input_usuario_dia > 31:
#             print("Data inválida")
#             break
#         else:
#             pass
#         input_usuario_mes = int(input("Insira o mês: "))
#         if input_usuario_mes < 1 or input_usuario_mes > 12:
#             print("Mês inválido")
#             break
#         else:
#             pass
#         input_usuario_ano = int(input("Insira o ano: "))
#         if input_usuario_ano < 0 or input_usuario_ano > 3000:
#             print("Ano inválido")
#             break
#         else:
#             print(f'{input_usuario_ano}-{input_usuario_mes}-{input_usuario_dia}')
#             break

# # variáveis criadas para testar a função
# print("Insira sua data no formato dd/mm/aaaa")
# input_usuario_dia = int(input('dd ')) 
# input_usuario_mes = int(input('mm '))
# input_usuario_ano = int(input('aaaa '))

def formatar_data_tentativa2(input_usuario_dia, input_usuario_mes, input_usuario_ano):
    try:
        data_usuario = datetime.date(input_usuario_ano, input_usuario_mes, input_usuario_dia)
        #print(f'Data informada: {input_usuario_dia}/{input_usuario_mes}/{input_usuario_ano}')
        data_formatada = data_usuario.isoformat()
        #print(f'Data formatada: {data_formatada}')
        return data_formatada
    except ValueError as e:
        print(f'Erro: {e}. Certifique-se de inserir uma data válida.')

# testando:
#exemplo = formatar_data_tentativa2(input_usuario_dia, input_usuario_mes, input_usuario_ano)
# print(exemplo)