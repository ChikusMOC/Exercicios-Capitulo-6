"""
Exercicio 17
"""


while True:
    try:
        num = int(input("Digite um numero inteiro positivo: "))
        if num <= 0:
            raise ValueError('Você digitou um numero negativo')
        else:
            break
    except ValueError:
        print('Você digitou um numero invalido.')

aux = 0
soma = 0
while aux <= num:
    soma = soma + aux
    aux = aux + 1
print(f'Somatorio usando while {soma}')
soma = 0
for i in range(0, num+1):
    soma = soma + i
print(f'Somatorio usando for {soma}')
