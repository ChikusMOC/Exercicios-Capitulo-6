"""
Exercicio 32
"""

from random import randint
dado1 = []
dado2 = []
while True:
    try:
        num = int(input("Informe um numero: "))
        for i in range(0, abs(num)):
            dado1.append(randint(1, 6))
            dado2.append(randint(1, 6))
        print(f'{dado1}\n{dado2}')
        for i in range(0, abs(num)):
            if dado1[i] == dado2[i]:
                print(f'{dado1[i]} = {dado2[i]}')
            elif dado1[i] < dado2[i]:
                print(f'{dado1[i]} < {dado2[i]}')
            elif dado1[i] > dado2[i]:
                print(f'{dado1[i]} > {dado2[i]}')
        break
    except ValueError:
        print("Você digitou algo errado, tente de novo.")