import datetime

def calcular_idade(data_nascimento):
    """
    Calcula a idade com base na data de nascimento fornecida.

    Args:
        data_nascimento (str): Data de nascimento no formato "dd/mm/aaaa".

    Returns:
        int: A idade calculada em anos.
    """
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    data_atual = datetime.date.today()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

