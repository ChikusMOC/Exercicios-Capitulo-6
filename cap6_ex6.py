"""
Exercicio 6 -
"""


aux = 0
soma = 0
while aux < 10:
    number = float(input('Digite um numero: '))
    soma = soma + number
    aux = aux + 1
print(f'Media dos valores digitados é {soma/10}')