from data_util import calculo_idade
from data_util import ano_bissexto
from data_util import formatar_data

#calcular a idade com a pessoa inserindo a data de nascimento "aaaa-m-dd"
data_nascimento = input("insira sua data de nascimento no formato aaaa-m-dd: ")
idade = calculo_idade.calcular_idade(data_nascimento)
print(idade)

#formatar a data se ela inserir dd/mm/aaaa para aaaa-mm-dd
data_nascimento = input("insira sua data de nascimento no formato dd/mm/aaaa: ")
data_formatada = formatar_data.data
print(data_formatada)

#verificar se um ano é bissexto ou não
ano = input("Inisira o ano que deseja verificar se é bissexto ou não: ")
print(ano_bissexto.eh_ano_bissexto(ano))