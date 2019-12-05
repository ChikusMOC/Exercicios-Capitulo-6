"""
Exercicio 40
"""


lista = []
while True:
    try:
        num = int(input('Informe um numero: '))
        if num >= 0:
            lista.append(num)
        else:
            break
    except ValueError:
        print('Algo deu errado')
print(f'Menor numero informado foi o {max(lista)}')
print(f'Menor numero informado foi o {min(lista)}')
