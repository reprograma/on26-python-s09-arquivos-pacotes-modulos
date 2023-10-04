from datetime import datetime

def calcAge(dateOfBirth):
    dateOfBirth = datetime.strptime(dateOfBirth, "%d/%m/%Y")
    today = datetime.now()
    age = today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
    return age