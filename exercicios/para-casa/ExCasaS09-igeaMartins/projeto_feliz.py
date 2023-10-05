from data_util.ano_bissexto import define_ano_bissexto
from data_util.calculo_idade import age
from data_util.formatar_data import formatar_data_dma_amd
from datetime import date

#Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.

print(age(date(int(input('Informe o ano do seu aniversário: ')), int(input(', informe o mês: ')), int(input(', informe o dia: ')))))

#Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`

print(define_ano_bissexto(int(input('Informe um ano pra saber se ele é bissexto: '))))

#Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd".
print('Converter formato brasileiro para formato ISO')
print(formatar_data_dma_amd(int(input('Informe o dia: ')), int(input('Informe o mês: ')), int(input('Informe o ano: '))))



