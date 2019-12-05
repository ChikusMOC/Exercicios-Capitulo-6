"""
Exercicio 2 -
"""

aux1 = 0
aux2 = 1
print('Começando o loop em for.')
for _ in range(3):
    for i in range(1, 101):
        print(i, end=" ")
print('\nComeçando o loop em while.')
while aux1 < 3:
    while aux2 < 101:
        print(aux2, end=" ")
        aux2 = aux2 + 1
    aux2 = 1
    aux1 = aux1 + 1

