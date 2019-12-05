"""
Exercicio 43
"""

lista = []
while True:
    try:
        idade = int(input('Digite uma idade: '))
        if idade == 0:
            break
        else:
            lista.append(idade)
    except ValueError:
        print('Algo deu errado.')

try:
    print(f'Media de idades informada = {(sum(lista))/len(lista)}')
except ZeroDivisionError:
    print('Você finalizou o programa sem informar idades.')
