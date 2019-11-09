import numpy as np

np.random.seed(1)
a = np.random.normal(size=10)
print(a)

a > 0
print(a[3:6])

b = [True, False, False, False, False, False, False, False, False, False]
print(a[b])


#Maiores que 0
print("Maior que zero")
b = a > 0
print(a[b])

#Menor que 0
print("Maior que zero")
b = a < 0
print(a[b])

print(a[(a > -0.5) & (a < 0.5)])
# print(a[-0.5 < a < 0.5])
