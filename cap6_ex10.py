"""
Exercicio 10 -
"""


#  forma 1
soma = 0
aux = 0
for i in range(1, 1000):
    if i % 2 == 0:
       soma = soma + i
       aux = aux + 1
    if aux == 50:
        break

print(f'foma com for com auxiliar {soma}')

#  forma 2
soma = 0

for i in range(0, 101, 2):
    soma = soma + i

print(f'foma com for sem auxiliar {soma}')

#  forma 3
aux = 0
soma = 0

while aux <= 100:
    if aux % 2 == 0:
        soma = soma + aux
    aux = aux + 1
print(f'foma com while {soma}')
