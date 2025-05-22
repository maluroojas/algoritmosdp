import random

#exericio 1 - como imprimir cada um dos elementos:
lista = [1, 2, 3, ['beto', 'ifms', [3.14, 3.15, 3,16]]]
#resolução:
def imprimir_elementos(l):
    for elemento in l:
        if isinstance(elemento, list):
            imprimir_elementos(elemento)
        else:
            print(elemento)

imprimir_elementos(lista)

#Exercício 2 - sistema de eleição:
'''
ler mil votos para escolher 1 de 3 candidatos

qtd de votos do candidato 1 e a %
qtd de votos do candidato 2 e a %
qtd de votos do candidato 3 e a %
qtd de votos do candidato brancos ou nulos e a %

apresente qual foi o candidato com o maior e o menor numero de votos
'''
#resolução:
# Inicializa os contadores de votos
votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0
votos_nulos = 0

# Coleta de votos
for i in range(1000):
    voto = int(input(f"Voto {i + 1}: "))
    
    if voto == 1:
        votos_cand1 += 1
    elif voto == 2:
        votos_cand2 += 1
    elif voto == 3:
        votos_cand3 += 1
    else:
        votos_nulos += 1

# Cálculo das porcentagens
total_votos = 1000
porc1 = (votos_cand1 / total_votos) * 100
porc2 = (votos_cand2 / total_votos) * 100
porc3 = (votos_cand3 / total_votos) * 100
porc_nulos = (votos_nulos / total_votos) * 100

# Exibição dos resultados
print("\nRESULTADO FINAL")
print(f"Candidato 1: {votos_cand1} votos ({porc1:.2f}%)")
print(f"Candidato 2: {votos_cand2} votos ({porc2:.2f}%)")
print(f"Candidato 3: {votos_cand3} votos ({porc3:.2f}%)")
print(f"Brancos/Nulos: {votos_nulos} votos ({porc_nulos:.2f}%)")

# Determinação do mais e menos votado entre os candidatos
votos_dict = {
    "Candidato 1": votos_cand1,
    "Candidato 2": votos_cand2,
    "Candidato 3": votos_cand3
}

mais_votado = max(votos_dict, key=votos_dict.get)
menos_votado = min(votos_dict, key=votos_dict.get)

print(f"\nMais votado: {mais_votado} com {votos_dict[mais_votado]} votos.")
print(f"Menos votado: {menos_votado} com {votos_dict[menos_votado]} votos.")

#Exercicio 3 - Escolha de vinhos:
'''
leia uma quantidade infinita de escolhas de vinhos, entre: 1 - seco, 2 - tinto, 3 - sem preferencia.
O sistema para quando o usuario decidir parar.
'''
#resolução:
# Inicializa os contadores
seco = 0
tinto = 0
sem_preferencia = 0

print("Escolha o tipo de vinho:")
print("1 - Seco")
print("2 - Tinto")
print("3 - Sem preferência")
print("0 - Encerrar")

while True:
    escolha = int(input("Digite sua escolha: "))

    if escolha == 0:
        break
    elif escolha == 1:
        seco += 1
    elif escolha == 2:
        tinto += 1
    elif escolha == 3:
        sem_preferencia += 1
    else:
        print("Opção inválida. Tente novamente.")

# Exibe o resultado
print("\nRESULTADO DAS ESCOLHAS:")
print(f"Vinhos secos: {seco}")
print(f"Vinhos tintos: {tinto}")
print(f"Sem preferência: {sem_preferencia}")

#Exercicio 4 - listas de listas:
'''
leia uma lista(5mil elementos), onde cada lista interna contem 3 valores: [numero, idade, sexo]

imprima o numero, idade e sexo de cada pessoa
'''
#resolução

pessoas = []

for i in range(1, 5001):
    numero = i
    idade = random.randint(1, 100)
    sexo = random.choice(["M", "F"])
    pessoas.append([numero, idade, sexo])

# Imprime os dados de cada pessoa
for pessoa in pessoas:
    numero, idade, sexo = pessoa
    print(f"Número: {numero}, Idade: {idade}, Sexo: {sexo}")