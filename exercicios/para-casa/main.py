from datetime import datetime
from datautil import anobissexto, calculoidade, formatardata

data = input("\n Insira uma data no formato dd/mm/aaaa: ")
data_formatada = formatardata.formatardata(data)
ano_nascimento = int(data.split("/")[-1])

idade_calculada = calculoidade.calcularidade(data)

if anobissexto.ano_bissexto(int(data.split("/")[-1])):
    print("\n Ano não bissexto")
else:
    print("\n Ano bissexto")

print(f"\n {idade_calculada} anos de idade")