"""
Exercicio 13 -
"""


while True:
    try:
        num = int(input("Digite um numero inteiro par: "))
        if num <= 0:
            raise ValueError('Você digitou um numero impar')
        elif num % 2 == 0:
            break
        else:
            raise ValueError('Você digitou um numero impar')
    except ValueError:
        print('Você digitou um numero invalido.')

aux = 0
while aux <= num:
    print(aux, end=' ')
    aux = aux + 2
print('\n')
for i in range(0, num+1, 2):
    print(i, end=' ')
