# Anomalia - tudo que está fora de 2x o desvio padrão

import pandas as pd
import numpy as np

df = pd.read_csv('household_power_consumption.txt', delimiter=';', na_values=['?'])
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
val_between_2006_2009 = df[(df.ano >= 2006) & (df.ano <= 2009)]
val_2010 = df[df.ano == 2010]

mean = val_between_2006_2009.Voltage.mean()
std = val_between_2006_2009.Voltage.std()

# O Abs é feito para os valores negativo. Gera uma series (array) de boolean.
anomalias = (val_2010.Voltage - mean).abs() > 2 * std
print(val_2010[anomalias])