from datetime import date
# Exercício feito em grupo 

# def formatar_data(data):
#     # recebe uma data no formato dd/mm/aaaa
    # formata a data para o formato aaaa-mm-dd

# data_atual = date.today() #como receber uma data informada pelo usuário?
data_informada = input('Informe a data desejada no formato aaaa/mm/dd: ')
data_formatada = date.strftime(data_informada, '%d/%m%Y')
print(data_formatada)
