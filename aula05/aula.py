import random 

x = random.randint(0,10)

escolha = ['gelado', 'quente']

y = random.choice(escolha)

#listas tuplas e dicionário

#listas - são coleções de objetos, podem ser d qualquer tipo

nome ='beto'

#sintaxe

lista = ['A', 'B', 'C', 'ifms', 2025, 3.14]

#indice = 0

#imprimindo a lista

print (lista)

for i in range (6):
    print(lista [i])
    
for item in lista:
    print(item)
    
#acessar /inserir

print(lista [-1])

lista [2] = 'beto'

lista.append('U2')

#Ordenar 
#lista. sort()

#Inverte a lista

lista.reverse()

#contar tamanho da estrutura

print(len(lista))

for i in range (len(lista)):
    print(lista[i])
    
for i, item in enumerate(lista):
    print (f'O item de indice {i} tem o valor {item}')
    
'''
enumerate() retorna uma tupla de dois elementos a cada iteração: um número seuqencial item da sequencia
'''

#TUPLAS

'''
Semelantes a listas, porém são imutaveis !! n pode acrescentar, apagar, ou fazer atribuição
'''

#sintaxe

tupla = 1, 2, 3, 4

#oq determina os elementos d uma tupla são as virgulas, independente de parenteses 

print(tupla[0])

lista = [1, 2, 3 (2, 3, 4)]

#converter tupla em lista 
nova_lista = list(tupla)

#converter lista em tupla
nova_tupla = tuple(lista)

.

