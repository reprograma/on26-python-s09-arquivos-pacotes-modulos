from datetime import datetime

data = (input("Digite sua data de nascimento="))
data_nas = datetime.strptime(data, "%d/%m/%Y")
print(data_nas)