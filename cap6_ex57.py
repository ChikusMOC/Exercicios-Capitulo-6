"""
Exercicio 57
"""


def primos(num):
    primos = list(range(3, num + 1, 2))
    inicio = 0
    maximo = (num ** 0.5) // 2
    while inicio <= maximo:
        passo = (inicio * 2) + 3
        for i in range(inicio * (passo + 3) + 3, len(primos), passo):
            primos[i] = 0
        inicio += 1
        while inicio <= maximo:
            if primos[inicio] != 0:
                break
            inicio += 1
    primos = [2] + primos
    return [x for x in primos if x != 0]


while True:
    try:
        numa = int(input('Primeiro numero: '))
        numb = int(input('Segundo numero: '))
        if numb > numa:
            print(f'Interceção {numa} ate {numb} - {len([x for x in primos(numb) if x >= numa])}')
        elif numa > numb:
            print(f'Interceção {numb} ate {numa} - {len([x for x in primos(numa) if x >= numb])}')
        elif numb == numa:
            if numa in primos(numa):
                print(f'Voce informou um numero primo.')
            else:
                print('Você não informou um intervalo com numero primo.')
        else:
            raise ValueError
    except ValueError:
        print('Finalizando o Programa.')
        break

