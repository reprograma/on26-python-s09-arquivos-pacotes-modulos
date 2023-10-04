#Função leap_year(year) que verifica se um ano é bissexto e retorna True ou False.

import datetime

def isLeap(year):
    try:
        if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
            return f"The year {year} is a leap year.\n"
        else:
            return f"The year {year} is not a leap year.\n"
    except (ValueError, TypeError):
        return "Year must be inserted in the format YYYY.\n"