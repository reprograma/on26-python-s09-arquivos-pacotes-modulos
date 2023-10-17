from datetime import datetime

def formatar_data(data):
    data_obj = datetime.strftime(data, "%d/%m/%y")
    data_formatada = data_obj.strftime("%y-%m-%d")
    return data_formatada


