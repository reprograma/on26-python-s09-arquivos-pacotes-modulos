from datetime import datetime

def formatar(data):

    data_nas = datetime.strptime(data,"%Y-%m-%d")
    data_formatada = data_nas.strftime("%d/%m/%Y")
    return(data_formatada)

