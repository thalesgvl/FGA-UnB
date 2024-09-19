r = ''
c = s = maior = menor = 0
while r in 'Yy':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar [Y/N]?: ')).strip()[0]
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n


media = (s / c)
print('A média dos: {:.2f} valores digitados foi de: {}. O maior valor foi: {} e o menor foi: {}.'.format(c, media, maior, menor))
print('FIM.')
