"""
Exercicio 51
"""


from datetime import date
data = date.today()
sal = 2000
ano = 1995
aumento = 0.015 * 2000
while ano < data.year:
    sal += aumento
    print(sal)
    aumento += aumento
    ano += 1
print(f'Salario do funcionario no ano de {data.year} é {sal:.2f}')
