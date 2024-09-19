a1 = int(input('Primeiro termo da p.a: '))
r = int(input('Razão da p.a: '))
c = 0

print('{}'.format(a1), end= ' ->')

while c != 9:
    c += 1
    a1 += r
    print(' {}'.format(a1), end=' ->')
print(' FIM.')
