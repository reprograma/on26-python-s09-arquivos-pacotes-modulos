import json
dados = {
    "Thaysa Lima" : 20, 
    "Cesar Lima" : 24, 
    "Thayna Lima" : 28
}

with open("./dados.json", "w") as arq_json:
    dados = json.dump(dados,arq_json)
    #aqui ele leu, abra o arquivo "dados.json" e escreva os dados do dicionario "dados"