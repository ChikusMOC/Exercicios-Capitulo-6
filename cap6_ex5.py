"""
Exercicio 5 -
"""

aux = 0
soma = 0
while aux < 10:
    number = float(input('Digite um numero: '))
    soma = soma + number
    aux = aux + 1

print(f"A soma dos valores digitados é = {soma}")