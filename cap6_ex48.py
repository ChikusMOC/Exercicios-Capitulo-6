"""
Exercicio 48
"""
auxa, auxb, soma = 0, 1, 0

while auxa < 4000000:
    if auxa % 2 == 0:
       soma = soma + auxa
    print(auxa, end=' ')
    auxa, auxb = auxb, auxa + auxb

print(f'\nA soma dos pares é {soma}')
