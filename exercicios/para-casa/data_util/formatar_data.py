from datetime import datetime

def formatar_data(data_nascimento):
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        data_formatada = data_nascimento.strftime("%Y-%m-%d")
        return data_formatada
    except ValueError:
        return None