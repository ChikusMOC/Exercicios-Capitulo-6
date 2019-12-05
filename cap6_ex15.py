"""
Exercicio 15
"""

while True:
    try:
        num = int(input("Digite um numero inteiro impar: "))
        if num <= 0:
            raise ValueError('Você digitou um numero par')
        elif num % 2 != 0:
            break
        else:
            raise ValueError('Você digitou um numero invalido')
    except ValueError:
        print('Você digitou um numero invalido.')

aux = 1
while aux <= num:
    print(aux, end=' ')
    aux = aux + 2
print('\n')
for i in range(1, num+1, 2):
    print(i, end=' ')
