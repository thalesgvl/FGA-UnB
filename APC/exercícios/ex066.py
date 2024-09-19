c = s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print('Foram digitados: {} números, a soma entre eles foi de: {}.'.format(c, s))
