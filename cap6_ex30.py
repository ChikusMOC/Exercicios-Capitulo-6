"""
Exercicio 30
"""
sinal = 1
soma = 0
num = int(input("Informe um numero: "))

for i in range(1, num+1):
    soma = soma + i
print(f'Sequencia 1+2+3+4+5+...+n = {soma}')

soma=0
for i in range(1, 2*num):
    soma = soma + sinal*i
    sinal = -sinal
print(f'Sequencia 1-2+3-4+5-...+(2n-1) = {soma}')

soma = 0
for i in range(1, 2*num, 2):
    soma = soma + i
print(f'Sequencia 1+3+5+7+...+(2n-1) = {soma}')
