"""
Exercicio 55
"""


def primo(num1):
    aux = 0
    if num1 != 0 and num1 != 1:
        for i in range(2, num1):
            if num1 % i == 0:
                aux = aux + 1
    return aux


while True:
    try:
        num = int(input('Digite um numero: '))
        if num > 0:
            soma = 0
            i = 0
            for aux in range(num**2):
                if primo(aux) == 1:
                    soma = soma + aux
                    i += 1
                    if i == num:
                        break

            print(soma)
        else:
            print('Digite um numero maior que 0.')
    except ValueError:
        print('Erro do sistema')
        break
