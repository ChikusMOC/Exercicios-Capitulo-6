"""
Exercicio 52
"""


while True:
    try:
        valor = int(input('Valor a ser retirado: '))
        aux = 0
        while valor != 0:
            if valor//100 > 0:
                aux = valor//100
                print(f'notas de 100 {aux}')
                valor = valor - (valor//100) * 100
            elif valor % 100 > 0:
                if valor >= 50:
                    print(f'Notas de 50 {valor//50}')
                    valor = valor - (valor // 50) * 50
                elif valor >= 20:
                    print(f'notas de 20 {valor//20}')
                    valor = valor - (valor // 20) * 20
                elif valor >= 10:
                    print(f'Notas de 10 {valor//10}')
                    valor = valor - (valor // 10) * 10
                elif valor % 10 >= 5:
                    print(f'notas de 5 {valor//5}')
                    valor = valor - (valor // 5) * 5
                elif valor % 10 >= 2:
                    print(f'notas de 2 {valor//2}')
                    valor = valor - (valor // 2) * 2
                elif valor % 10 >= 1:
                    print(f'notas de 1 {valor}')
                    valor = valor - valor
        break
    except ValueError:
        print('Erro do sistema.')

