import datetime  # Importa a biblioteca datetime para trabalhar com datas.

def calcular_idade(data_nascimento):
    # Converte a data de nascimento para um objeto datetime
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    
    # Obtém a data atual
    data_atual = datetime.datetime.now()
    
    # Calcula a diferença de anos entre a data de nascimento e a data atual
    idade = data_atual.year - data_nascimento.year
    
    # Verifica se já fez aniversário neste ano
    if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
        idade -= 1
        
    return idade  # Retorna a idade calculada com base na data de nascimento.
