from data_util.calculo_idade import calcular_idade
from data_util.ano_bissexto import eh_ano_bissexto
from data_util.formatar_data import formatar_data
import datetime

def main():
    """
    Programa principal para calcular idade, verificar ano bissexto e formatar data.

    Este programa solicita a data de nascimento do usuário, verifica se o ano atual é bissexto
    e formata uma data inserida pelo usuário.
    """
    # Solicitar data de nascimento
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    idade = calcular_idade(data_nascimento)
    print(f"Sua idade é {idade} anos.")

    # Verificar se o ano atual é bissexto
    ano_atual = datetime.datetime.now().year
    if eh_ano_bissexto(ano_atual):
        print(f"{ano_atual} é um ano bissexto.")
    else:
        print(f"{ano_atual} não é um ano bissexto.")
        
        # Solicitar data no formato "dd/mm/aaaa" e formatar
    data_input = input("Digite uma data (dd/mm/aaaa): ")
    data_formatada = formatar_data(data_input)
    print(f"A data formatada é: {data_formatada}")

if __name__ == "__main__":
    main()
