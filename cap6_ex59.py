"""
Exercicio 59
"""


def cadastro():
    consumo = float(input('Consumo no mês: '))
    while True:
        try:
            codigo = int(input('Codigo do consumidor: '))
            if codigo >= 1 and codigo <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            print('Codigos de 1 a 3.')
    return [codigo, consumo]

while True:
    try:
        hab = int(input('Numero de habitantes: '))
        vkwh = float(input('Valor kwh: '))
        lista = []
        soma1 = 0
        soma2 = 0
        soma3 = 0
        for i in range(hab):
            lista.append(cadastro())
        for i in range(hab):
            if lista[i].__getitem__(0) == 1:
                soma1 = soma1 + lista[i].__getitem__(1)
            elif lista[i].__getitem__(0) == 2:
                soma2 = soma2 + lista[i].__getitem__(1)
            elif lista[i].__getitem__(0) == 3:
                soma3 = soma3 + lista[i].__getitem__(1)
        maior = lista[0].__getitem__(1)
        menor = lista[0].__getitem__(1)
        for i in range(hab):
            if maior < lista[i].__getitem__(1):
                maior = lista[i].__getitem__(1)
            if menor > lista[i].__getitem__(1):
                menor = lista[i].__getitem__(1)
        print(f'O maior consumo foi R$ {maior} ou {maior/vkwh:.2f} Horas')
        print(f'O menor consumo foi R$ {menor} ou {menor/vkwh:.2f} Horas')
        print(f'A media de consumo dos habitantes foi de R$ {(soma1+soma2+soma3)/hab} '
              f'ou {((soma1+soma2+soma3)/hab)/vkwh} Horas')
        print(f'O consumo total da categoria 1 foi de R$ {soma1} ou {soma1/vkwh:.2f} Horas\n'
              f'O Consumo total da categoria 2 foi de R$ {soma2} ou {soma2/vkwh:.2f} Horas\n'
              f'O Consumo total da categoria 3 foi de R$ {soma3} ou {soma3/vkwh:.2f} Horas')
    except ValueError:
        print('Erro')
        break
