#Importe os módulos do pacote "date_modules" e use as funções para realizar as seguintes tarefas:

#Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.

#Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`.

#Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd".

from date_modules import format_date
from date_modules import leap_year
from date_modules import calc_age

print("\nTest module format_date inserting the correct date format")
print(format_date.formatDate("27/06/1990"))

print("\nTest module format_date inserting the wrong date format")
print(format_date.formatDate("06/27/1990"))

print("\nTest module calcAge inserting the correct date format")
print(calc_age.calcAge("27/06/1990"), "years old")

print("\nTest module calcAge inserting the wrong date format")
print(calc_age.calcAge("06/27/1990"))

print("\nTest module leap_year inserting a commum year with the correct format")
print(leap_year.isLeap(2023))

print("\nTest module leap_year inserting a leap year with the correct format")
print(leap_year.isLeap(2020))

print("\nTeste com inserção de formato de ano incorreto")
print(leap_year.isLeap("2023"))