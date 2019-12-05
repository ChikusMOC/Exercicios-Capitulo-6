"""
Exercicio 28
"""


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


h = 0
aux = 0
while True:
    try:
        num = int(input("Digite um numero inteiro positivo: "))
        if num < 0:
            print('Informe um numero POSITIVO')
        else:
            for i in range(1, num+1):
                aux = fatorial(i)
                h = h + 1/aux
            print(f'{h+1:.2f}')
            break
    except ValueError:
        print('Você digitou um numero invalido.')