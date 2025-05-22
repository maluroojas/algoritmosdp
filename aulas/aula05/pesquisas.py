#PESQUISAS 

#insert, pop, tipos de ordenação
#set, frozenset

# Criação de uma lista
lista = [10, 20, 30]

# Inserindo o número 15 na posição 1 (segunda posição)
lista.insert(1, 15)

# A lista agora fica assim:
print(lista)  # Saída: [10, 15, 20, 30]

# Lista de exemplo
lista = [10, 20, 30]

# Remove o item da posição 1 (valor 20)
removido = lista.pop(1)

print(removido)  # Saída: 20 (valor que foi removido)
print(lista)     # Saída: [10, 30]

# Remove o último item (30)
lista.pop()
print(lista)     # Saída: [10]

lista = [5, 3, 1, 4, 2]

# Cria uma nova lista ordenada (original não muda)
ordenada = sorted(lista)

print(ordenada)  # [1, 2, 3, 4, 5]
print(lista)     # [5, 3, 1, 4, 2] (sem alterações)

lista = [5, 3, 1, 4, 2]

# Ordena a lista original
lista.sort()

print(lista)  # [1, 2, 3, 4, 5]

lista = [1, 2, 3, 4, 5]

# Ordena de forma decrescente
lista.sort(reverse=True)

print(lista)  # [5, 4, 3, 2, 1]

# Lista com números repetidos
numeros = [1, 2, 2, 3, 4, 4, 5]

# Convertendo em set (conjunto)
conjunto = set(numeros)

print(conjunto)  # {1, 2, 3, 4, 5} – remove duplicatas automaticamente

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # União: {1, 2, 3, 4, 5}
print(a & b)  # Interseção: {3}
print(a - b)  # Diferença: {1, 2}

# Criando um conjunto imutável
conjunto = frozenset([1, 2, 3])

# Não é possível adicionar ou remover itens
# conjunto.add(4)  # Isso causaria um erro!

print(conjunto)  # Saída: frozenset({1, 2, 3})

