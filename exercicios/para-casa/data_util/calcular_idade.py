
from datetime import datetime
def calcular_idade(data):

    ano = int(input('Digite o ano do nascimento:'))
    mes = int(input('Digite o mês do nascimento:'))
    dia = int(input('Digite o dia do nascimento:'))


    data = datetime(ano, mes, dia)
    datahoje= datetime.now()
    idadepessoa= datahoje - data

    dia = idadepessoa.days
    anos, dias = dia // 365, dia % 365
    mes, dia = dia //30, dias % 30

    print('sua idade é: {} anos'. format (anos))