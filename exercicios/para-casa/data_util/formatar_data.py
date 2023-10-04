import datetime

def formatar_data(data):
    data = datetime.datetime.strptime(data, "%d/%m/%Y")
    return data.strftime("%d/%m/%Y")
    

if __name__ == "__main__":
    data = "17/11/2000"
    data_formatada = formatar_data(data)
    print(data_formatada)