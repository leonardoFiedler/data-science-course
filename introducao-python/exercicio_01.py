
# Obter o valor da coluna e imprimir as informacoes

def ler_valor2():
    while True:
        valor = input("Digite uma coluna")
        try:
            yield int(valor)
        except:
            raise StopIteration()