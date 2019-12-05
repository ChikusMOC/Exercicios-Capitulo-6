"""
Exercicio 26
"""


while True:
    try:
        num = int(input("Digite um numero inteiro: "))
        if num % 11 == 0:
            print(f'Numero {num} é multiplo de 11')
            break
        elif num % 13 == 0:
            print(f'Numero {num} é multiplo de 13')
            break
        elif num % 17 == 0:
            print(f'Numero {num} é multiplo de 17')
            break
        else:
            print('Continue a informar numeros, condição de parada numeros multiplos de 11, 13 ou 17')
    except ValueError:
        print('Você digitou um numero invalido.')
