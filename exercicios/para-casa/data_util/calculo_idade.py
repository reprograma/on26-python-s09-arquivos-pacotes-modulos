#Contém uma função calcular_idade(data_nascimento) 
# que recebe uma data de nascimento como argumento e retorna a idade da pessoa.

#Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e 
#use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.

from datetime import date, time, datetime

def calcular_idade(data_nascimento):
    idade = (datetime.date - data_nascimento)
    return calcular_idade
    
    
data_nascimento = input("Digite sua data de nascimento:")
data_atual = datetime.now()
data_nascimento = datetime.strptime(data_nascimento, "%Y%m%d")

print(calcular_idade)



    