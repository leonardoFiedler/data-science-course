import numpy as np
import pandas as pd


class DeteccaoAnomalia:

    def __init__(self, df, coluna):
        self._coluna = coluna
        self._mean = df[coluna].mean()
        self._std = df[coluna].std()

    def detectar(self, df):
        return np.abs(df[self._coluna] - self._mean) > (2 * self._std)

# para execucao na Main
if __name__ == '__main__':
    df = pd.read_csv('household_power_consumption.txt', delimiter=';', na_values=['?'])
    df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
    val_between_2006_2009 = df[(df.ano >= 2006) & (df.ano <= 2009)]
    val_2010 = df[df.ano == 2010]

    modelo = DeteccaoAnomalia(val_between_2006_2009, coluna='Voltage')
    anomalias = modelo.detectar(val_2010)
    print(val_2010[anomalias])

