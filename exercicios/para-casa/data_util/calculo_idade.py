from datetime import date, time, datetime
def calculo_idade (data_nascimento):
    return idade_atual

ano_atual= int(input('Digite o ano atual: '))
data_nascimento = input('Digite a data de nascimento: ')
data= data_nascimento =  datetime.strptime(data, "%d/%m/%Y")

idade_atual = (datetime.now() - data_nascimento)
print(idade_atual)

