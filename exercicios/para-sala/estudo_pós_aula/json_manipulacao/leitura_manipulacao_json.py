import requests

requerimento = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(requerimento)
print(f"\t{requerimento.json()}")

rick_jerry = requests.get("https://rickandmortyapi.com/api/character/5")
print(rick_jerry)
print("********")
print(rick_jerry.json()["name"])