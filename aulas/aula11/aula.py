#reduce

from functools import reduce
from random import randint

'''
sintaxe
reduce(func, array)
'''

numeros = [randint (1, 500) for _ in range (10)]

#numeros = [1, 2, 3, 4, 5, 6, 7, 8]
soma_total = reduce(lambda x, y: x + y, numeros)

'''
maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero 

print(f"A lista de numeros é: {numeros}")
print(f"O maior numero na lista é: {maior_numero}")
'''
#só consegui com for

#resolução do professor

maior = reduce(lambda x, y: x if x > y else y, numeros)





