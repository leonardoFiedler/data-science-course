import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# idades = np.random.normal(24, 50, 1000)
# (_, ax) = plt.subplots(1, 1, figsize=(15, 10))
# ax.hist(idades, bins=26)
# ax.set_title('Histograma')
# ax.set_xlabel('idades')
# ax.set_ylabel('quantidades')
# plt.savefig('grafico.png')

# idades2 = np.random.normal(24, 50, 1000)
# (_, ax) = plt.subplots(1, 1, figsize=(15, 10))
# ax.scatter(idades, idades2)
# ax.set_title('Scatter')
# ax.set_xlabel('idades')
# ax.set_ylabel('quantidades')
# plt.savefig('grafico.png')

# corr = idades + np.sin(idades)
# (_, ax) = plt.subplots(1, 1, figsize=(15, 10))
# ax.scatter(idades, corr)
# ax.set_title('Scatter')
# ax.set_xlabel('idades')
# ax.set_ylabel('quantidades')
# plt.savefig('grafico.png')


df = pd.read_csv('household_power_consumption.txt', delimiter=';', na_values=['?'])
df['dia'] = df.Date.apply(lambda x: int(x.split('/')[0]))

