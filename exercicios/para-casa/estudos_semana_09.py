from datetime import datetime, timedelta

# Manipulando datas

hoje = datetime.now()
print(hoje) # fornece a data e o horário
print(hoje.date()) # fornece somente a data, sem o horário, no formato aaaa/mm/dd
print(hoje.day)

# Fazendo contas com as datas
# Necessário importar o método timedelta

amanha = hoje + timedelta(days=1)
print(amanha)

## CRIANDO UMA DATA ESPECÍFICA

data_contrato = datetime(year=2022, month=9, day=1)
print(data_contrato.date())
