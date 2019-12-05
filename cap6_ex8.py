"""
Exercicio 8 -
"""


aux = 0
lista = []
while aux < 10:
    number = float(input('Digite um numero: '))
    lista.append(number)
    aux = aux + 1

lista.sort()
print(lista)
