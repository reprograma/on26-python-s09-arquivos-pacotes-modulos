from datetime import date, time, datetime, timedelta

def formatar(data):
   data = datetime.strptime(data, "%d/%m/%Y")
   data_formatada = data.strftime("%Y/%m/%d")
   return data_formatada
data = (input("Digite a data que desejar atualizar="))
#print(f'O seu grande dia é {data_formatada}')

#def formatar():
   # data= datetime.strftime(data, "%d%m/%Y")
    #data_formatada = data.strftime("%d/%m/%Y")
    #return(data_formatada)
#data = (input("Digite sua data de nascimento="))
#print(formatar())

#data = (input("Digite sua data de nascimento="))
#data_nas = datetime.strptime(data, "%d/%m/%Y")
#data_formatada = data_nas.strftime("%d/%m/%Y")
#print(data_formatada)
