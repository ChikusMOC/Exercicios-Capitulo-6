"""
Exercicio 22
"""

lista = []
while True:
    try:
        num = float(input("Informe uma nota válida: "))
        if num >= 10 and num <= 20:
            lista.append(num)
        else:
            break
    except ValueError:
        print('Valor informado não é valido')
print(f'Média das notas informada = {(sum(lista)/len(lista)):.2f}')
