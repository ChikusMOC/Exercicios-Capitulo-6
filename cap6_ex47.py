"""
Exercicio 47
"""


class calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adicao(self):
        print(self.num1 + self.num2)

    def subtracao(self):
        print(self.num1 - self.num2)

    def multiplicacao(self):
        print(self.num1 * self.num2)

    def divisao(self):
        print(self.num1 / self.num2)


while True:
    try:
        op = int(input('1 - Adição.\n2 - Subtração.\n3 - Multiplicação.\n4 - Divisão.\n5 - Sair.\nOpção: '))
        if op == 1:
            num1 = int(input('Numero que deseja somar: '))
            num2 = int(input('Numero que deseja somar: '))
            calc = calculadora(num1, num2)
            calc.adicao()
        elif op == 2:
            num1 = int(input('Numero que deseja subtrair: '))
            num2 = int(input('Numero que deseja subtrair: '))
            calc = calculadora(num1, num2)
            calc.subtracao()
        elif op == 3:
            num1 = int(input('Numero que deseja multiplicar: '))
            num2 = int(input('Numero que deseja multiplicar: '))
            calc = calculadora(num1, num2)
            calc.multiplicacao()
        elif op == 4:
            num1 = int(input('Numero que deseja dividir: '))
            num2 = int(input('Numero que deseja dividir: '))
            if num2 == 0:
                print('Não existe divisão por 0')
                raise ValueError
            else:
                calc = calculadora(num1, num2)
                calc.divisao()
        elif op == 5:
            break
        else:
            raise ValueError
    except ValueError:
        print('Algo deu errado.')
