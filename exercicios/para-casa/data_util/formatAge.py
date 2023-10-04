from datetime import datetime

def formatAge(date):
    dateObj = datetime.strptime(date, "%d/%m/%Y")
    dataFormatada = dateObj.strftime("%Y-%m-%d")
    return dataFormatada