# recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd"
from datetime import datetime

data = datetime.strptime("16/07/1996", "%d/%m/%Y").date()

def formatar_data(data):
    return data.strptime("%Y-%m-%d")
