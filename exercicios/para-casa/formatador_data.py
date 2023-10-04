from data import formato_data

data = input("Digite uma data (no formato original): ")
formato_querido = input("Digite o formato desejado (por exemplo, '(%d/%m/%Y'): ")

data_formatada = formato_data(data, formato_querido)
print(f"A data formatada: {data_formatada}")
