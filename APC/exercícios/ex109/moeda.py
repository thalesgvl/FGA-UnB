def dobro(preco = 0, format=False):
    res = preco * 2
    return res if not format else moeda(res)


def metade(preco = 0, format=False):
    res = preco / 2
    return res if not format else moeda(res)


def aumentar(preco = 0, taxa = 0, format=False):
    res = preco + (preco * taxa/100)
    return res if not format else moeda(res)


def diminuir(preco = 0, taxa = 0, format=False):
    res = preco - (preco * taxa/100)
    return res if not format else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')
