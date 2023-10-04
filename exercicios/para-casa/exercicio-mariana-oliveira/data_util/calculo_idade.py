import datetime as dt


#data_de_nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ") 

#print(hoje.date())
def calcular_idade(data_de_nascimento):
    """este bloco passa a data_de_nascimento de estring para o formato data 
    e atribui à variável dia_atual a data do dia de hoje"""
    data_de_nascimento = dt.datetime.strptime(data_de_nascimento, '%d/%m/%Y')
    dia_atual = dt.datetime.now()
    
    """ Verifica se o mês de aniversário da pessoa já passou. 
    Neste caso, a idade dela será o ano atual menos o ano de nascimento"""
    if dia_atual.month - data_de_nascimento.month > 0:
        idade = dia_atual.year - data_de_nascimento.year
        return idade
    #Verifica se o mês de aniversário da pessoa ainda não passou.
    #Neste caso, ela ainda não fez aniversário, então sua idade é o ano atual - o ano de nascimento -1
    elif dia_atual.month - data_de_nascimento.month < 0:
        idade = (dia_atual.year - data_de_nascimento.year) - 1
        return idade    
    #Verifica se a estamos no mês de aniversário da pessoa. Neste caso, se hoje for o dia 
    #exato do aniversário dela ou se o dia do aniversário já passou, a idade dela será calculada por ano atual - ano de nascimento
    elif dia_atual.month - data_de_nascimento.month == 0: 
        if dia_atual.day >= data_de_nascimento.day:
            idade = dia_atual.year - data_de_nascimento.year
        else:
            idade = (dia_atual.year - data_de_nascimento.year) - 1     
        return idade
    