n = int(input('Digite um número: '))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m{}\033[m'.format(i), end=' ')
        c += 1
    else:
        print('{}'.format(i), end=' ')
print('\nO número: {}. Foi divisível: {} vezes.'.format(n, c))
if c > 2:
    print('Portanto, o número: {}. Não é primo.'.format(n))
if c == 2:
    print('Portanto, o número: {}. É primo!'.format(n))
