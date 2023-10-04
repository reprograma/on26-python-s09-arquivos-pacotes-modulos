from datetime import datetime

def idade(data_nascimento):
    data_atual = datetime.now()
    data_nascimento = datetime.strptime (data_nascimento,'%Y-%m-%d')

    idade = data_atual - data_nascimento

    return idade

data_nascimento = (input('Digite o ano de seu nascimento: '))

print(idade)