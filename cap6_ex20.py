"""
Exercicio 20
"""


lista = [0, 0]
lista_tot_num = []
lista_pares = []

while True:
    try:
        num = int(input("Informe um numero (ou 1000 para finalizar): "))
        if num == 1000:
            break
        elif num % 2 == 0:
            lista[1] = lista[1] + 1
            lista[0] = lista[0] + 1
            lista_pares.append(num)
            lista_tot_num.append(num)
        else:
            lista[0] = lista[0] + 1
            lista_tot_num.append(num)
    except ValueError:
        print("Você digitou algo errado, tente de novo.")

print(f'Foram informados um total de {lista[0]} numeros e {lista[1]} pares')
print(f'os numeros pares são {lista_pares}')
print(f'a lista de numero informados {lista_tot_num}')
