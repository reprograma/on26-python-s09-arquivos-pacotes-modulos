#Função format_date(date) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd".

import datetime

def formatDate(date):
    received_date_format = "%d/%m/%Y"
    pattern_date_format = "%Y-%m-%d"
    try:
        date_obj = datetime.datetime.strptime(date, received_date_format)
        formatted_date = date_obj.strftime(pattern_date_format)
        return(formatted_date)
    except ValueError:
        return "Invalid date format. Please use the following format: DD/MM/AAAA.\n"