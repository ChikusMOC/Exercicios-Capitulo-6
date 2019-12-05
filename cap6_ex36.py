"""
Exercicio 36
"""

soma = 0
soma1 = 0
for i in range(1, 101):
    soma += i**2
for i in range(1, 101):
    soma1 += i
print(f'Diferença entre a soma dos quadrados({soma}) e o quadrado da'
      f' soma({soma1**2}) é igual a {soma1**2-soma}')
