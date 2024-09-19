listagem = ('Lápis', 2.90, 
            'Borracha', 4.90,
            'Caderno', 14.90,
            'Estojo', 25.90,
            'Compasso', 9.90,
            'Mochila', 120.90,
            'Livro', 35.90,
            'Canetas', 22.90)
print('=' * 40)
print('{:^40}'.format('Listagem de preços.'))
print('=' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print(' R${:>7.2f}'.format(listagem[pos]))
print('=' * 40)
