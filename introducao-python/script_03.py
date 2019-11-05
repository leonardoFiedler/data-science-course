def somar(*lista, **kwargs):
    soma = 0
    for v in lista:
        soma += v * kwargs['peso']
    return soma

print(somar(1, 2, 3, peso=2))