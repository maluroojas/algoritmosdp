from random import randint

#dicionarios 

#Praticando 

'''
crie um programa que leia o nome de 5 alunos, e suas 4 notas
verifique qual aluno teve a maior média e mostro no final
a % de alunos aprovados e reprovados
'''

alunos = {}

# Leitura dos dados 
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota de {nome}: "))
        notas.append(nota)
    alunos[nome] = notas

# Cálculos
maior_media = 0
melhor_aluno = ""
aprovados = 0
reprovados = 0

for nome, notas in alunos.items():
    media = sum(notas) / 4
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome
    if media >= 6:
        aprovados += 1
    else:
        reprovados += 1

# Resultados
print("\nRESULTADOS FINAIS")
print(f"Aluno com a maior média: {melhor_aluno} - Média: {maior_media:.2f}")
print(f"Percentual de aprovados: {(aprovados / 5) * 100:.2f}%")
print(f"Percentual de reprovados: {(reprovados / 5) * 100:.2f}%")
