"""
Exercicio 37
"""


num = 0
for i in range(1000, 10000):
    num = ((i // 100) + (i % 100))
    if num**2 == i:
        print(i)
