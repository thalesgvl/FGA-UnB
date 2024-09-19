a1 = int(input('Primeiro termo da p.a: '))
razao = int(input('Razão da p.a: '))
c = 0
continuar = 9
contador_total = 0
resp = ''

print('{}'.format(a1), end= ' ->')

while resp != 0:
    for i in range(continuar):
        c += 1
        a1 += razao
        print(' {}'.format(a1), end=' ->')
    print(' PAUSA.', end='')
    resp = int(input('\nQuantos termos você quer mostrar a mais?: '))
    contador_total += continuar
    continuar = resp

print('Progressão aritmética finalizada com: {} termo mostrados.'.format(contador_total + 1))
print(' FIM.')
