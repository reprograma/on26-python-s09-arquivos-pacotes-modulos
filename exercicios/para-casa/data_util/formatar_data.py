from datetime import datetime

def formatar_data(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
    return data_formatada