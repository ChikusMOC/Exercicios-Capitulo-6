"""
Exercicio 25
"""
#  Forma 1 - Usando for
soma = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(f'Usando for {soma}')
#  Forma 2 - Usando while
soma = 0
aux = 0

while aux < 1000:
    if aux % 3 == 0 or aux % 5 == 0:
        soma += aux
    aux += 1
print(f'Usando while {soma}')
