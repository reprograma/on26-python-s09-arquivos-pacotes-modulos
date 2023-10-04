from data_util import calculo_idade
from data_util import formatar_data
from data_util import ano_bissexto
from datetime import datetime

data_nascimento_srt = input('Digite sua data de nascimento (dia/mês/ano): \n')
print(f'Formato inicial da data: \n{data_nascimento_srt}')

data_de_hoje = datetime.now().date()
data_de_hoje_formatada = data_de_hoje.strftime("%d/%m/%Y")

print(f'A data de hoje é: {data_de_hoje_formatada}')

print('\n*** Cálculo da idade ***')

data_nascimento = datetime.strptime(data_nascimento_srt,  "%d/%m/%Y")


print (f'Sua Idade é:\n {calculo_idade.calcular_idade (data_nascimento)}  anos')


print (f'Novo formato da data de nascimento: \n {formatar_data.formatar_data(data_nascimento)} ')
print (f'Novo formato da data de hoje: \n {formatar_data.formatar_data(data_de_hoje)} ')

ano_atual = int(data_de_hoje_formatada[-4:])
print( f'O ano de  { ano_atual} é Bissexto?\n {ano_bissistema de equações linearessexto.eh_ano_bissexto(ano_atual)}')

data_nascimento_formatada = data_nascimento.strftime("%d/%m/%Y")
ano_nascimento = int(data_nascimento_formatada[-4:])
print( f'O ano de  { ano_nascimento}, seu ano de nascimento, é Bissexto?\n {ano_bissexto.eh_ano_bissexto(ano_nascimento)}')
