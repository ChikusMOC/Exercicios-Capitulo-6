"""
Exercicio 34
from math import gcd

lista = list(range(1, 10))
a = lista[0]
for i in lista[1:]:
    a = a*i // gcd(a, i)
    print(a)
print(a)
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        print(a)
    return a


aux = 1
for i in range(1, 21):
    aux = aux*i // gcd(aux, i)
print(aux)
