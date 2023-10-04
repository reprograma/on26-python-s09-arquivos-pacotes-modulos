#biblioteca datetime
#mostrando as componentes de data
from datetime import date, time, datetime, timedelta
date_hora = datetime(2023,10,4)
print(date_hora.strftime("%B"))

#mostrando hora e data atuais
hoje = date.today().strftime('%d/%m/%Y')
agora = datetime.now().strftime('%d/%m/%Y %H:%M')
print(hoje)
print(agora)

#formatando a data 
#data=input("1997/09/01")
#data_nas = datetime.strptime(data,"%Y-%m-%d")
#data_formatada = data_nas.strftime("%d/%m/%Y")
#print(data_formatada)

#formatando usando fromisoformat
data = date.fromisoformat("2023-10-04")
print(data.strftime("%Y %B %d"))

#objeto de hora
hora = time(hour=16, minute=20)
print(hora)
hora_agora = datetime.now()
print(hora_agora)

#usando o delta, vc pode adicionar, remover dias, horas, minutos e segundos
data_futura = datetime.today() + timedelta(days=20)
print(data_futura)
data_passada = datetime.today() - timedelta(days=29)
print(data_passada)