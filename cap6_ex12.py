"""
Exercicio 12 -
"""


while True:
    try:
        num = int(input("Digite um numero inteiro positivo: "))
        if num < 0:
            raise ValueError('Você digitou um numero negativo')
        else:
            break
    except ValueError:
        print('Você digitou um numero invalido.')

aux = num
while aux >= 0:
    print(aux, end=' ')
    aux -= 1

print('\n')
for i in range(num, -1, -1):
    print(i, end=' ')

