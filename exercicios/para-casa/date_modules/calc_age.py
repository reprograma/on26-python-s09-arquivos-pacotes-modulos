# Função calc_age(birthdate) que recebe uma data de nascimento como argumento e retorna a idade da pessoa.

import datetime
  
def calcAge(birthDate): 
    today = datetime.date.today() 
    received_date_format = "%d/%m/%Y"
    try:
        date_obj = datetime.datetime.strptime(birthDate, received_date_format)
        age = today.year - date_obj.year - ((today.month, today.day) < (date_obj.month, date_obj.day))
        return f"{age} years old\n"
    except (ValueError, TypeError):
        return "Invalid date format. Please use the following format DD/MM/AAAA.\n"
      
