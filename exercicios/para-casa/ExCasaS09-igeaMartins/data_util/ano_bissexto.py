def define_ano_bissexto(year):
    if (year%4 == 0 and year%100 != 0) or (year%4 == 0 and year%100 == 0 and year%400 == 0):
        print('O ano é bissexto')
    else:
        print('O ano não é bissexto')
