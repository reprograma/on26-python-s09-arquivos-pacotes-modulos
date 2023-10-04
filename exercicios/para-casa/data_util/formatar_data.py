from datetime import datetime
def formatar_data(data):
  print(datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d"))

