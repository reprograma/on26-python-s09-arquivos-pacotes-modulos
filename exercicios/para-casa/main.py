from data_util.calcAge import calcAge
from data_util.leapYear import isLeapYear
from data_util.formatAge import formatAge


dateOfBirth = input("Digite sua data de nascimento (dd/mm/aaaa): ")
age = calcAge(dateOfBirth)
print(f"Sua idade é: {age} anos")


currentYear = int(input("Digite o ano atual: "))
if isLeapYear(currentYear):
    print(f"{currentYear} é um ano bissexto.")
else:
    print(f"{currentYear} não é um ano bissexto.")


dataFormatar = input("Digite uma data (dd/mm/aaaa): ")
dataFormatada = formatAge(dataFormatar)
print(f"A data formatada é: {dataFormatada}")