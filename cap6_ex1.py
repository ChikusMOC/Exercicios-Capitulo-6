"""
Exercicio 1 -
"""
contador = 0

while True:
    for i in range(1, 100):
        if i % 3 == 0:
            contador = contador + 1
            print(f'multiplos de 3 {i}')
        if contador == 5:
            break
    break

