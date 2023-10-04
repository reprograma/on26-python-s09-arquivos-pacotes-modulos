import data_util.calculo_idade as calculo_idade
import data_util.ano_bissexto as ano_bissexto
import data_util.formatar_data as formatar_data

while True:
    # Solicita ao usuário que insira a data de nascimento
    data_nascimento = input("Insira sua data de nascimento (dd/mm/aaaa): ")

    # Formata a data de nascimento usando o módulo formatar_data
    data_formatada = formatar_data.formatar_data(data_nascimento)

    if data_formatada:
        print(f"Data de nascimento formatada: {data_formatada}")

        # Extrai a data de nascimento 
        ano_nascimento = int(data_nascimento.split("/")[-1])
      
        # Calcula a idade usando o módulo calculo_idade
        idade = calculo_idade.calcular_idade(data_nascimento)
        print(f"Sua idade atual é: {idade} anos")

        # Verifica se o ano de nascimento é bissexto usando o módulo ano_bissexto
        if ano_bissexto.verificar_ano_bissexto(ano_nascimento):
            print(f"O ano  do seu nascimento: {ano_nascimento} é bissexto")
        else:
            print(f"O ano  do seu nascimento: {ano_nascimento} não é bissexto")
        break
    
    else:
        print("Data de nascimento inválida. Certifique-se de usar o formato dd/mm/aaaa.")
