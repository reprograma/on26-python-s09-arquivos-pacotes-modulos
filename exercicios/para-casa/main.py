#Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.
from data_util import calculo_idade, formatar_datas, ano_bissexto

data_nascimento = int(input("Digite a data do seu nascimento, no formato dd/mm/aaaa: "))
idade = data_util.calculo_idade(data_nascimento)
print("Sua idade é ", {idade})

#Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`.
ano = input("Digite um ano: ")



#Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd".
data = input("Digite uma data no formato dd/mm/aaaa: ")
print(data)