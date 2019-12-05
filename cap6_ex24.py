"""
Exercicio 24
"""

soma = 0
while True:
    try:
        num = int(input("Informe um numero, ou digite 0 pra finalizar: "))
        if num == 0:
            break
        else:
            for i in range(1, abs(num)):
                if num % i == 0:
                    soma = soma + i
            print(soma)
            soma = 0
    except ValueError:
        print("Você digitou algo errado, tente de novo.")
