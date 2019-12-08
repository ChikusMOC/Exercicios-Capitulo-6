"""
Exercicio 58
"""


def primos(num):
    if num < 2:
        return []
    if num == 2:
        return [2]
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
        if numa < 2 or numb < 2:
            raise ValueError
        elif numb > numa:
            print(f'Interceção {numa} ate {numb} - {sum([x for x in primos(numb) if x >= numa])}')
        elif numa > numb:
            print(f'Interceção {numb} ate {numa} - {sum([x for x in primos(numa) if x >= numb])}')
        else:
            if numa in primos(numa):
                print(f'Como você informou um numero primo a soma da interceção é {numa}')
            else:
                print('Você não informou um intervalo com numero primo.')
    except ValueError:
        print('Finalizando o Programa.')
        break

