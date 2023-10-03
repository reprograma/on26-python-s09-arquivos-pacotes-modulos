from datetime import datetime



def formatar_data(data):
    data= datetime.now()
    print(data.day,'/',data.month,'/',data.year)

    data1= datetime.now()
    print(data1.year,'-',data1.month,'-',data1.day)
    
    return

#anotação:
# hoje = datetime.now()
# print(hoje.day,'-',hoje.month,'-',hoje.year)

