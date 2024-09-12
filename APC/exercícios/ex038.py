n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O valor: {} é maior que: {}.'.format(n1, n2))
elif n2 > n1:
    print('O valor: {} é maior que: {}.'.format(n2, n1))
else:
    print('O valor: {} é igual ao valor: {}.'.format(n1, n2))
