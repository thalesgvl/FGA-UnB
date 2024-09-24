def dobro(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res


def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')
