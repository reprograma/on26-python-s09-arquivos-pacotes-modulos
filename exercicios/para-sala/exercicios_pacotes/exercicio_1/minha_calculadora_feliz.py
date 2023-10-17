'''
**Exercício 1: Crie um Pacote de Matemática**

Crie um pacote Python chamado "matematica" que inclua módulos para realizar operações matemáticas básicas,
como adição, subtração, multiplicação e divisão.
Crie um programa principal que importe esses módulos e realize operações matemáticas com eles.
'''


from matematica import calculo

a = 3
b = 2


print(f'A soma é: {calculo.soma(a, b)}')

print(f'A subtração é: {calculo.subtracao(a, b)}')

print(f'A multiplicacao é: {calculo.multiplicacao(a, b)}')

print(f'A divisão é: {calculo.divisao(a, b)}')
