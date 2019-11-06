from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

(X, y) = load_iris(return_X_y=True)
data = train_test_split(X, y, test_size=0.2, random_state=1)
(X_train, X_test, y_train, y_test) = data

# Numero do K - quantidade de itens a serem verificados e separados
k = 5

labelsResults = []
for i in range(len(X_test)):
    x = X_test[i, :]
    d = X_train - x
    d = np.square(d).sum(axis=1)
    
    sortedMatDis = np.argsort(d)
    labels = []
    for j in range(k):
        idx = sortedMatDis[j]
        labels.append(y_train[idx])

    labelsResults.append(pd.value_counts(labels).idxmax())

print(labelsResults)
print('Score:', accuracy_score(y_test, labelsResults))