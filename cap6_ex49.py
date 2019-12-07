"""
Exercicio 49
"""

while True:
    try:
        salcarlos = int(input('Valor do salario: '))
        saljoao = salcarlos / 3
        print(f'Salario de Joao = {saljoao:.2f}')
        meses = 0
        while saljoao <= salcarlos:

            salcarlos = salcarlos + (salcarlos * 0.02)
            saljoao = saljoao + (saljoao * 0.05)
            meses += 1
        break
    except ValueError:
        print('Erro do sistema.')
print(f'Total de meses necessarios para passar ou igualar o salario = {meses}')
print(f'Salario final de Carlos = {salcarlos:.2f}\nSalario final de Joao = {saljoao:.2f}')
