import numpy

# numeros = [0, 1, 2, 3, 4.2, 5, 6, 7, 8, 9]

# for numero in numeros:
#     print(numero)
    
# print("Range")
# for i in range(len(numeros)):
#     print(i, numeros[i])
    
# list(range(3, 10))

# contador = 0
# while contador < len(numeros):
#     print(contador, numeros[contador])
#     contador += 1
    
# valor = 5
# if valor > 10:
#     print("Maior que 10")
# else:
#     print("Menor que 10")

# while True:
#     valor = input("Digite um numero")
#     try:
#         valor = int(valor)
#         print(type(valor))
#     except ValueError:
#         print("Entrada e invalida")
#         break
    
#     if eh_par(valor):
#         print(f'{valor} é par')
#     else:
#         print(f'{valor} é impar')

def ler_valor():
    lista = []
    while True:
        valor = input("Digite um numero")
        try:
            lista.append(int(valor))
        except ValueError:
            break

    return lista

# O yield funciona semelhante a um await. É uma função generator que retorna um valor, mas retorna para continuar a execucao.
def ler_valor2():
    while True:
        valor = input("Digite um numero")
        try:
            yield int(valor)
        except:
            raise StopIteration()

def eh_par(x):
    return x % 2 == 0

for valor in ler_valor2():
    if eh_par(valor):
        print(f'{valor} é par')
    else:
        print(f'{valor} é impar')

