from datetime import datetime


def data_formatada(data):
    data_obj = datetime.strptime(data, '%d/%m/%Y')
    data_formatada = data_obj.strftime('%Y/%m/%d')
    return data_formatada


