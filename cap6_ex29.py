"""
Exercicio 29 -
"""
from math import factorial

h = 0

for i in range(1, 5):
    h = h + i/factorial(i*2)
print(f'{h:.2f}')