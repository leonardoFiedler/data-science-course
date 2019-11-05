import numpy as np

# DICA: Olhar o itertools do Python: import itertools

idades = np.random.randint(24, 50, 31)
# for idade in sorted(idades):
#     print(idade)

# for (i, idade) in enumerate(idades):
#     print(i, idade)

# print(list(enumerate(idades)))
# print(sum(idades))

idades2 = np.random.randint(24, 50, 31)

# for i in range(len(idades)):
#     print(i, idades[i], idades2[i])

# O comando zip retorna uma tupla para duas listas
# for (idade1, idade2) in zip(idades, idades2):
#     print(idade1, idade2)

# for (i, (idade1, idade2)) in enumerate(zip(idades, idades2)):
#     print(i, idade1, idade2)

media = idades.mean()
diffs = []

# Formas diferentes de fazer o diff com a media
# Por meio de for
# for idade in idades:
#     diffs.append(idade - media)
# print(diffs)

# Por meio de comprehension
# diffs = [idade - media for idade in idades]
# print(diffs)

diffs = filter(lambda idade: idade % 2 == 0, idades)
diffs = map(lambda idade: idade - media, diffs)
print(next(diffs))
