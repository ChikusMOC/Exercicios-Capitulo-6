"""
Exercicio 38
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = num1 ** 2 + num2 **2
soma = soma ** 0.5
print(f'Termo pitagorico é a={num1} b={num2} c={soma:.2f} \nonde a²+b²=c² = {num1}²+{num2}²={soma:.2f}²'
      f'\n{num1**2}+{num2**2}={soma**2:.2f}')
