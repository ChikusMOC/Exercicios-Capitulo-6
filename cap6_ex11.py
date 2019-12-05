"""
Exercicio 11 -
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
#  forma 1 - usando while
i = 0
print('Usando while')
while i <= num:
    print(i, end=' ')
    i += 1

#  forma 2 - usando for
print('\nUsando for')
for a in range(0, num+1):
    print(a, end=' ')
