"""
Exercicio 54
"""


def primo(num):
    if num != 0 and num != 1:
        if num > 3:
            for i in range(2, num):
                if num % i == 0:
                    return False
        return True
    return False


while True:
    try:
        num = int(input('Valor: '))
        if primo(num):
            print('Primo')
        else:
            print('Não é primo')
    except ValueError:
        print('Erro no sistema')
        break
