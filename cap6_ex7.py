"""
Exercicio 7 -
"""


aux = 0
soma = 0
while aux < 10:
    number = int(input('Digite um numero: '))
    if number >= 0:
        soma = soma + number
        aux = aux + 1
    else:
        print("Não aceitamos numeros negativos.")

print(f'Media dos valores digitados é {soma/10}')
