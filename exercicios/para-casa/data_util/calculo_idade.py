from datetime import datetime 
 
def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    idade = data_atual - data_nascimento
    idade = idade.days// 365
    return idade
    
    