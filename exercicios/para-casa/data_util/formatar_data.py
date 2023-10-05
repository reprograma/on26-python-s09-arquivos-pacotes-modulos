from datetime import datetime

def formatar_data(data_original):
    data_formatada = datetime.strptime(data_original, '%d/%m/%Y')
    return data_formatada.date()

dia = (input('Informe o dia desejado: '))
mes = (input('Informe o mês desejado: '))
ano = (input('Informe o ano desejado: '))
data_original = dia + '/' + mes + '/' + ano
data_formatada = formatar_data(data_original)
print(data_formatada)