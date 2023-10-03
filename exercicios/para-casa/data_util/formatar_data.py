import datetime

def formatar_data(data):
    """
    Formata uma data no formato "dd/mm/aaaa" para "aaaa-mm-dd".

    Args:
        data (str): Data no formato "dd/mm/aaaa".

    Returns:
        str: A data formatada no formato "aaaa-mm-dd".
    """
    data_obj = datetime.datetime.strptime(data, "%d/%m/%Y")
    data_formatada = data_obj.strftime("%Y-%m-%d")
    return data_formatada
