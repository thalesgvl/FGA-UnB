def dobro(preco = 0, format=False):
    res = preco * 2
    return res if not format else moeda(res)


def metade(preco = 0, format=False):
    res = preco/2
    return res if not format else moeda(res)


def aumentar(preco = 0, taxa = 0, format=False):
    res = preco + (preco * taxa/100)
    return res if not format else moeda(res)


def descontar(preco = 0, taxa = 0, format=False):
    res = preco - (preco * taxa/100)
    return res if not format else moeda(res)


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco, aumento, desconto):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'O dobro de {moeda(preco)} é: \t{dobro(preco, True)}')
    print(f'A metade de {moeda(preco)} é: {metade(preco, True)}')
    print(f'Aumentando 15%, temos: \t{aumentar(preco, aumento, True)}')
    print(f'Diminuindo 35%, temos: \t{descontar(preco, desconto, True)}')
    print('-' * 40)