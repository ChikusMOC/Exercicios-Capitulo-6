"""
Exercicio 39
"""


while True:
    try:
        base = int(input("Valor da base: "))
        altura = int(input("Valor da altura: "))
        if base <= 0 or altura <= 0:
            print('Você informou valores errados.')
        else:
            print(f'A area do triangulo é {(base*altura)/2}')
            break
    except ValueError:
        print('Algo deu errado.')
