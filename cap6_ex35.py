"""
Exercicio 35
"""

print('Este programa irá calcular a soma dos impares no intervalo informado, caso deseja encerrar informe um '
      'intervalo invalido')
while True:
    try:
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
        if num1 < num2:
            soma = 0
            for i in range(num1, num2 + 1):
                if i % 2 != 0:
                    soma = soma + i
            print(f'Soma dos impares neste intervalo: {soma}')

        else:
            break
    except ValueError:
        print('Alguma coisa deu errado.')
