import datetime  # Importa a biblioteca datetime para trabalhar com datas.

def formatar_data(data):
    # Converte a data no formato "dd/mm/aaaa" para "aaaa-mm-dd".
    data_formatada = datetime.datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
    return data_formatada  # Retorna a data formatada no novo formato.
