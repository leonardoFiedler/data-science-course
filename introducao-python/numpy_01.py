import numpy as np
from numpy import mean

idades = np.random.randint(24, 50, size=31)
# Media
# print(idades.mean())
print(int(np.mean(idades)))
print(mean(idades))

# Mediana
print(int(np.median(idades)))


idades1 = np.random.randint(24, 50, size=31)
idades2 = np.random.randint(24, 50, size=31)

diff = idades1 - idades2
print(diff)
print(diff.mean())

# Distribuicao normal - maior valor em 30 com desvio de 3 (para cima e para baixo)
idades1 = np.random.normal(30, 3, size=31).astype(np.int)
idades2 = np.random.normal(30, 3, size=31).astype(np.int)

print(idades1)
