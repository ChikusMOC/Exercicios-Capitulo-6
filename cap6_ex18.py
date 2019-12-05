"""
Exercicio 18
"""
import sys
from collections import Counter

while True:
    try:
        loop = int(input("Quantos numero deseja informar? "))
        if loop < 0:
            raise ValueError('Numero informado não pode ser negativo.')
        elif loop == 0:
            sys.exit()
        else:
            break
    except ValueError:
        print("Você digitou algo errado, tente de novo.")

lista = []
for i in range(0, loop):
    num = int(input('Digite um numero: '))
    lista.append(num)

print(f'maior numero informado {max(lista)}')
aux = 0
for i in lista:
    if i == max(lista):
        aux = aux + 1
print(f'quantidade de vezes que ele aparece usando for {aux}')
aux = 0
i = 0
while i <= loop-1:
    if lista[i] == max(lista):
        aux = aux + 1
    i = i + 1
print(f'quantidade de vezes que ele aparece usando while {aux}')
