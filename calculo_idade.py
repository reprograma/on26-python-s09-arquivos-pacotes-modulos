# Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa.

def data_formatar():

    data_nascimento = datetime.strptime(data,"%Y-%m-%d")
    data_formatada = data_nascimento.strftime("%d/%m/%Y")
    return(data_formatada)

data=input("Digite a data de nascimento:")
print(data_formatar())