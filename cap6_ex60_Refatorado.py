"""
Exercicio 60
"""


while True:
    try:
        lista = []
        while True:
            try:
                num = int(input("Numero: "))
                if num == 0:
                    raise ValueError
                else:
                    lista.append(num)
            except ValueError:
                break
        if len(lista) > 0:
            print(f'Soma dos numeros digitados = {sum(lista)}')
            print(f'Quantidade de numeros digitados = {len(lista)}')
            print(f'A media dos numeros digitados é = {(sum(lista)/len(lista)):.2f}')
            print(f'Maior numero digitado foi o {max(lista)}')
            print(f'Menor numero digitado foi o {min(lista)}')
            print(f'Media dos numeros pares é = '
                  f'{sum([x for x in lista if x % 2 == 0])/len([x for x in lista if x % 2 == 0]):.2f}')
            break
        else:
            raise ValueError
    except ValueError:
        print('Finalizando o Programa')
        break
