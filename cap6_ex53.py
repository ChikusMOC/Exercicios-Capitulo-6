"""
Exercicio 53
"""

while True:
    try:
        num = int(input('numero: '))
        c = 1
        for i in range(num + 1):
            for j in range(1, i+1):
                print(f'{c}', end=" ")
                c += 1
            print()
    except ValueError:
        print('Erro do sistema')
        break