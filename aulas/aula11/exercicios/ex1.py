import random 

def media_quadrados_pares (lista):
    pares = [num for num in lista if num % 2 == 0]
    quadrados = [num ** 2 for num in pares]
    
    if len(quadrados) == 0:
        return 0
    
    media = sum(quadrados) / len(quadrados)
    return media

lista_aleatoria = [random.randint(1, 20) for _ in range (20) for _ in range (10)]
print("Lista gerada:", lista_aleatoria)

resultado = media_quadrados_pares(lista_aleatoria)
print("Media dos quadrados dos numeros pares:", resultado)