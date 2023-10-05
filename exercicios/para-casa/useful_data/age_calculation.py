from datetime import datetime

def calculate_age(date_of_birth_str):
    try:
        # Converte a str data de nascimento em objeto datetime
        date_of_birth = datetime.strptime(date_of_birth_str, "%d/%m/%Y")
    
        # Mostra a data atual
        today = datetime.today()

        # Cálculo entre a data atual e data de nascimento
        # Verifica se o mês e dia de nascimento já ocorretam no ano atual
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    
        return age
    except ValueError:
        return None