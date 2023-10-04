# Contém uma função formatar_data(data) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd"
import datetime

def formatar_data(data):
    string_data = str(datetime.date.isoformat(data))[:10]
    return string_data