import json


estoque = {
    "produto1": {"nome": "Camiseta", "preco": 19.99, "quantidade": 100},
    "produto2": {"nome": "Calça Jeans", "preco": 39.99, "quantidade": 50},
    "produto3": {"nome": "Tênis", "preco": 49.99, "quantidade": 30},
}


with open("estoque_ex5.json","w") as arquivo_json:
    json.dump(estoque, arquivo_json)


with open("estoque_ex5.json", "r") as arquivo_json:
    dados_estoque = json.load(arquivo_json)

print("Dados do estoque:")
for produto, info in dados_estoque.items():
    print(f"Produto: {produto}")
    print(f"Nome: {info['nome']}")
    print(f"Preço: R${info['preco']:.2f}")
    print(f"Quantidade disponível: {info['quantidade']}")
    print()
