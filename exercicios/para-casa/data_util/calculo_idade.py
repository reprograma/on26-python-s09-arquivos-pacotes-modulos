from datetime import datetime
def calcular_idade (data_nascimento):
  ano_atual = datetime.today().year
  ano_nascimento = int(data_nascimento.split("/")[-1])
  idade = ano_atual - ano_nascimento
  return idade