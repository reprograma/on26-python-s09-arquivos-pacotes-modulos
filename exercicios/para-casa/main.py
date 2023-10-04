from data_util import calculo_idade
from data_util import ano_bisexto
from data_util import formatar_data

#calculando a idade a partir do módulo calculo_idade, usando a função idade
#nascimento = input("Digite a data de nascimento: ")
#idade = calculo_idade.calcular_idade(nascimento)
#print(f'sua idade é de {idade}anos')

#print(calculo_idade.calcular_idade(1997))

#conferirindo se o ano é bisexto a partir do módulo ano_bisexto usando a fução verificar_bi
#ano=input("Digiteo ano que deseja verificar:")
print(ano_bisexto.verificar_bi(2024))

#formatando data a partir do módulo formatar_data usando a função formatar
#data=input("Digite a data de nascimento")
#data_nas = datetime.strptime(data,"%Y-%m-%d")
#data_formatada = data_nas.strftime("%d/%m/%Y")
#print(data_formatada)
 
data = input("Digite a data que deseja formatar")
print(formatar_data.formatar(data))
