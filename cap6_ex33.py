"""
Exercicio 33
"""


numeros, aux = [], 0

while True:
    try:
        num = int(input('n: '))
        i = int(input('i: '))
        j = int(input('i: '))
        while len(numeros) < num:
            if aux % i == 0 or aux % j == 0:
                numeros.append(aux)
            aux += 1
        break
    except ValueError:
        print('Tente de novo.')
print(numeros)
