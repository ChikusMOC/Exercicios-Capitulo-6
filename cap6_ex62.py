"""
Exercicio 62

from num2words import num2words

total = ""

for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')
    total += num.replace(' ', '')

print(f'Entre 1 e 1000 temos {len(total)} letras.')
"""
#  a = [len('um'), len('dois'), len('trez'), len('quatro'), len('cinco'), len('seis'), len('sete'), len('oito'), len('nove')]
a = len('umdoistrezquatrocincoceisseteoitonove')
b = len('dezonzedozetrezequadorzequinzedezesseisdezessetedezoitodezenove')
c = len('vintetrintaquarentacinquentasessentasetentaoitentanoventa')
d = len('cento')
h = len('duzentostrezentosquatrocentosquinhentosseicentossetessentosoitocentosnovecentos')
e = len('e')
f = len("mil")
g = len("cem")

soma = 10*b + 90*a + 100*c + d*99 + f + 1611*e + g + 100*h
print(soma)
