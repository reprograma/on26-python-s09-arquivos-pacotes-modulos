import datetime as dt

def formatar_data(data):
    data = dt.datetime.strptime(data, '%d/%m/%Y')
    return data.date()