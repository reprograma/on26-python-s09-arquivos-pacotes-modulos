from datetime import datetime
#from para-casa import main

def formatar():

    data_nas = datetime.strptime(data_nas,"%Y-%m-%d")
    data_formatada = data_nas.strftime("%d/%m/%Y")
    return(data_formatada)

