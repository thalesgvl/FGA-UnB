s = 0
s2 = 0
for i in range(6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
    else:
        s2 += n
print('A soma dos números pares foi de: {}.'.format(s))
print('A soma dos números ímpares doi de: {}.'.format(s2))