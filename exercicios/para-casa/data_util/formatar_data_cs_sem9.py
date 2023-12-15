from datetime import datetime

def formatar_data(data):
    data_objeto = datetime.strptime(data, "%y-%m-%d")
    data_formatada = data_objeto.strftime("%d/%m/%y")
    return data_formatada


# Função para formatar a data do estilo americano (transforma string p/tempo) para o que a gente usa(dia-mês-ano).
# strptime serve para criar um objeto datetime, enquanto strftime formata um objeto datatime