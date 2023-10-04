# Importe as funções dos módulos do pacote "data_util"
from data_util.calculo_idade import calcular_idade
from data_util.ano_bissexto import eh_ano_bissexto
from data_util.formatar_data import formatar_data

def main():
    # Solicite ao usuário que insira sua data de nascimento
    data_nascimento = input("Digite sua data de Nascimento (dd/mm/aaaa): ")    

    # Use a função calcular_idade do módulo calculo_idade para calcular a idade da pessoa
    idade = calcular_idade(data_nascimento)
    
    print(f"Sua idade é {idade} anos.")
    
    # Verifique se o ano atual é bissexto
    ano_atual = int(input("Digite o ano atual: "))
    if eh_ano_bissexto(ano_atual):
        print(f"{ano_atual} é um ano bissexto.")
    else:
        print(f"{ano_atual} não é um ano bissexto.")
    
    # Solicite ao usuário que insira uma data no formato "dd/mm/aaaa"
    data_input = input("Digite uma data (dd/mm/aaaa): ")
    
    # Use a função formatar_data do módulo formatar_data para exibir a data no formato "aaaa-mm-dd"
    data_formatada = formatar_data(data_input)
    
    print(f"A data formatada é {data_formatada}.")

if __name__ == "__main__":
    main()  # Chama a função principal se o programa for executado diretamente
# if __name__ == "__main__": permite que você escreva código que será executado apenas quando o arquivo for executado diretamente como um programa, mas não quando for importado como um módulo em outro programa. Isso é útil para evitar a execução acidental de código quando você está apenas importando um módulo para reutilização em outros lugares.

# Entra em um loop infinito para permitir ao usuário continuar ou sair do programa
while True:
    deseja_continuar = input("Deseja continuar? Se não, digite 'Sair': ")
    if deseja_continuar.lower() == "sair":  # Verifica se o usuário quer sair do programa
        print("Saindo do programa...")
        break  # Sai do loop infinito se o usuário digitar 'Sair'
