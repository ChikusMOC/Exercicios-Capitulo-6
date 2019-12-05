"""
Exercicio 19
"""


while True:
    try:
        num = int(input("Informe um numero entre 100 e 999: "))
        if num < 100 and num > 999:
            raise ValueError('Numero informado não pode ser negativo.')
        else:
            break
    except ValueError:
        print("Você digitou algo errado, tente de novo.")

print(f'os algarismos que compõe o numero {num} são: {num//100} , {num//10-((num//100)*10)} e {num%10}')
