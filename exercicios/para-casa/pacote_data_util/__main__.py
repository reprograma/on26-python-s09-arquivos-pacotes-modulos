import modulos_data_util.modulo_calculo_idade as calcular_idade
import modulos_data_util.modulo_ano_bissexto as verificar_ano_bissexto
import modulos_data_util.modulo_formatar_data as formatar_data

while True:
    
    data_nascimento = input("Insira sua data de nascimento no formato 'dd/mm/aaaa': ")

    data_formatada = formatar_data.formatar_data(data_nascimento)

    if data_formatada:

        print(f"\nData de nascimento formatada: {data_formatada}")

        ano_nascimento = int(data_nascimento.split("/")[-1])

        idade = calcular_idade.calcular_idade(data_nascimento)
        print(f"\nSua idade atual é: {idade} anos")

        if verificar_ano_bissexto.verificar_ano_bissexto(ano_nascimento):
            print(f"\nO ano  do seu nascimento ({ano_nascimento}) é bissexto.\n")

        else:
            print(f"\nO ano  do seu nascimento ({ano_nascimento}) não é bissexto.\n")
            
        break

    else:
        print("\nA data informada é inválida. Utilize o formato 'dd/mm/aaaa'.\n")