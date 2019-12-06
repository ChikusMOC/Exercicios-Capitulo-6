"""
Exercicio 45
"""


while True:
    try:
        op = int(input('1 - km/h->m/s\n2 - m/s->km/h\n3 - Sair\nOpçãp: '))
        if op == 1:
            vel = float(input('Velocidade em kilometro por hora: '))
            print(f'Essa velocidade em metros por segundo é: {vel / 3.6:.2f}')
        elif op == 2:
            vel = float(input('Velocidade em metros por segundo: '))
            print(f'Essa velocidade em kilometros por hora é: {vel * 3.6:.2f}')
        elif op == 3:
            break
        else:
            raise ValueError
    except ValueError:
        print('Erro do sistema.')

