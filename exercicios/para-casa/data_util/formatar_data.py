def formatar_data(data):
    partes = data.split('/')
    if len(partes) != 3:
        return "Formato de data inválido. Use 'dd/mm/aaaa'."
    else:
        dia, mes, ano = partes
        return f"{ano}-{mes}-{dia}"
