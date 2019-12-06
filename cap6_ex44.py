"""
Exercicio 44
"""

while True:
    try:
        num = int(input('Digite um numero: '))
        auxa = 0
        auxb = 1
        if num >= 0:
            while True:
                print(auxa, end=" ")
                auxa, auxb = auxb, auxa + auxb
                if auxa > num:
                    print(auxa)
                    break
        else:
            print('Programa finalizado')
            break
    except ValueError:
        print('Algo deu errado.')

