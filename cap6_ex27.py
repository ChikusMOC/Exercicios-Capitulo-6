"""
Exercicio 27
"""

h = 0
while True:
    try:
        num = int(input("Digite um numero inteiro positivo: "))
        if num < 0:
            print('Informe um numero POSITIVO')
        else:
            for i in range(1, num+1):
                h = h + 1/i
            print(f'{h:.2f}')
            break
    except ValueError:
        print('Você digitou um numero invalido.')