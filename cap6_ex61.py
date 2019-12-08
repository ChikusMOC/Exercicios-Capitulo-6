"""
Exercicio 61
"""


i = 0
j = 0
num = 0
aux1 = 0
aux2 = 0
while i <= 999:
    j = i
    while j <= 999:
        pal = str(i * j)
        palInv = pal[::-1]
        if pal == palInv:
            auxpal = int(pal)
            if auxpal > num:
                num = auxpal
                aux1 = i
                aux2 = j
        j += 1
    i += 1

print(f'O maior palindromo de 3 digitos é {aux1} x {aux2} = {num}')
