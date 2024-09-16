a1 = int(input('Primeiro termo da p.a: '))
r = int(input('Razão da p.a: '))
a10 = a1 + (10 - 1) * r

for i in range(a1, a10 + r, r):
    print(' {}'.format(i), end=' ->')
print(' FIM.')