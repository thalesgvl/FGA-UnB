n = int(input('Digite um número: '))
print('{}!'.format(n))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print(f)
