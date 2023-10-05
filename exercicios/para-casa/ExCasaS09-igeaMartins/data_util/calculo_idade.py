from datetime import date

def age(birthdate):
    today = date.today()
    
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))

    int(one_or_zero)
    
    year_difference = today.year - birthdate.year
    
    age = year_difference - one_or_zero
    
    print('Sua idade é de ', age, 'ano(s).')