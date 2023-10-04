
from datetime import date
def calcular_idade(nascimento):
    hoje = date.today()
    data_nascimento = input("Digite sua data de nascimento=")
    parametro = ((hoje.month, hoje.day)<(data_nascimento.month, data_nascimento.day))
    diferença =  hoje.year - data_nascimento.year
    idade = diferença-parametro
    return idade
    print(idade)
    

#ano_atual =2023
#nascimento = int(input("Digite seu ano de nascimento="))
#idade = (ano_atual-nascimento)
#print(f'Sua idade é de {idade} anos.')
