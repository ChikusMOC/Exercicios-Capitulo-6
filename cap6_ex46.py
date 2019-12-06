"""
Exercicio 46
"""


from random import randint

while True:
    try:
        valor = randint(1, 1000)
        contador = 0
        while True:
            try:
                num = int(input('Qual o valor gerado? '))
                if num < valor:
                    print('Seu chute é menor que o numero.')
                elif num > valor:
                    print('Seu chute é maior que o valor')
                else:
                    print('Parabens você acertou o numero.')
                    break
                contador = contador + 1
            except ValueError:
                print('Erro do sistema.')
        break
    except ValueError:
        print('Erro do sistema')

print(f'Voce acertou na {contador+1} tentativa, parabens')
