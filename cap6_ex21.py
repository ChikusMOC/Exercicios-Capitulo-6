"""
Exercicio 21
"""
soma = 0
multi = 1
lista = []
i = 0
while i < 2:
    try:
        num = int(input("Informe um numero: "))
        lista.append(num)
        i = i + 1
    except ValueError:
        print('Valor informado não é valido')

lista.sort()
for i in range(lista[0], lista[1]+1):
    if i % 2 == 0:
        soma = soma + i
    else:
        multi = multi * i
print(f'Soma dos pares no intervalo {lista[0]} até {lista[1]} é igual a {soma}')
print(f'Multiplicação dos impares no intervalo {lista[0]} até {lista[1]} é igual a {multi}')
