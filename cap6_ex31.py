"""
Exercicio 31
"""


def impares(n):
    return n + 2


n = 1
soma = 0
for i in range(1, 51):
    soma = soma + n / i
    n = impares(n)

print(f'Resultado = {soma:.2f}')
