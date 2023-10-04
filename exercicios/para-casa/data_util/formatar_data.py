from datetime import datetime

def formatar(data):

    data_nascimento = datetime.strptime(data,"%Y-%m-%d")
    data_formatada = data_nascimento.strftime("%d/%m/%Y")
    return(data_formatada)

