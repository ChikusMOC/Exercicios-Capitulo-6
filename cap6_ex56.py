"""
Exercicio 56
Melhor resolução. Feita por MarcoAndreLopesMendes encontrada no site https://wiki.python.org.br/DeterminandoPrimos

def primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    nums = list(range(3, n+1, 2))
    nums_length = (n // 2) - 1 + (n % 2)
    idx = 0
    idx_sqrtn = int(n**0.5) // 2
    while idx <= idx_sqrtn:
        nums_at_idx = (idx << 1) + 3
        for j in range(idx * (nums_at_idx + 3) + 3, nums_length, nums_at_idx):
            nums[j] = 0
        idx += 1
        while idx <= idx_sqrtn:
            if nums[idx] != 0:
                break
            idx += 1
    return [2] + [x for x in nums if x != 0]

def meu_primos(limite):
    lista_de_primos = primes(limite)
    print(sum(lista_de_primos))
meu_primos(2000000)
"""


def primos(num):
    primos = list(range(3, num + 1, 2))
    inicio = 0
    maximo = (num ** 0.5) // 2
    while inicio <= maximo:
        passo = (inicio * 2) + 3
        for i in range(inicio * (passo + 3) + 3, len(primos), passo):
            primos[i] = 0
        inicio += 1
        while inicio <= maximo:
            if primos[inicio] != 0:
                break
            inicio += 1
    primos = [2] + primos
    return primos


print(sum(primos(2000000)))
