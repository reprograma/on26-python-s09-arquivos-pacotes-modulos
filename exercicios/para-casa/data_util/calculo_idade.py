import datetime

def calcular_idade(data_nascimento):
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    data_atual = datetime.datetime.now()
    diferenca_em_anos = (data_atual - data_nascimento).days / 365
    return diferenca_em_anos

if __name__ == "__main__":
  data_nascimento = "17/11/2000"
  idade = calcular_idade(data_nascimento)
  print(f"A idade da pessoa é de {idade:.2f} anos.")
