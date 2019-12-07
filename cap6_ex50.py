"""
Exercicio 50
"""


while True:
    ze = 110
    chico = 150
    tchico = 2
    tze = 3
    ano = 0
    while ze <= chico:
        ze += tze
        chico += tchico
        ano += 1
    break
print(f'Levou {ano} anos para Ze passar Chico.\nAltura Ze = {ze/100} e altura Chico = {chico/100}')
