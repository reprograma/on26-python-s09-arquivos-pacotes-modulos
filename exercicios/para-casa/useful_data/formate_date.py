def format_date(date):
    day, month, year = date.split('/')  # Método que divide a str data em dia, mês e ano
    formatted_date = f"{year}-{month}-{day}"  # novo formato em aaaa-mm-dd
    return formatted_date