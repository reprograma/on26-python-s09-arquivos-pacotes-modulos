def eh_ano_bissexto(ano):
    """
    Verifica se um ano é bissexto.

    Args:
        ano (int): O ano a ser verificado.

    Returns:
        bool: True se o ano for bissexto, False caso contrário.
    """
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
