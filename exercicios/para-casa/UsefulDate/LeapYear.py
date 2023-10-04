from datetime import date

def leap_year(year):
    if year%4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            print("Was born in a Leap year")
            return True
    else:
        print("It wasn't a leap year")
        return False
    