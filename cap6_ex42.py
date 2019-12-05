"""
Exercicio 42
"""


while True:
    try:
        num = int(input('Digite um numero: '))
        if num <= 0:
            break
        else:
            print(f'Quadrado = {num**2}\nCubo = {num**3}\nRaiz Quadrada = {num**0.5:.2f}')
    except ValueError:
        print('Algo deu errado')
