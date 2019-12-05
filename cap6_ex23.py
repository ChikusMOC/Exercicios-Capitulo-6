"""
Exercicio 23
"""


while True:
    try:
        num = int(input("Informe um numero positivo, ou digite 0 pra finalizar: "))
        if num < 0:
            raise ValueError('Numero informado não pode ser negativo.')
        elif num == 0:
            break
        else:
            for i in range(1, num + 1):
                if num % i == 0:
                    print(i, end=' ')
            print('\n')
    except ValueError:
        print("Você digitou algo errado, tente de novo.")
