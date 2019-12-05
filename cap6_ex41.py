"""
Exercicio 41
"""


while True:
    try:
        res1 = int(input('1ª Resistencia: '))
        res2 = int(input('2ª Resistencia: '))
        if res1 == 0 or res2 == 0:
            break
        else:
            print(f'Associação em paralelo igual a {((res1*res2)/(res1+res2)):.2f}')
    except ValueError:
        print('Algo deu errado')
