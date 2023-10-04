
from datetime import datetime

def formatar_data(data):
    data = datetime.strptime(data, "%d/%m/%Y")
    data_formatada = data.strftime("%Y-%m-%d")
    return data_formatada
