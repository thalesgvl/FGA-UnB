c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor?: '))
    c = 0
    if n == 0:
        break
    else:
        for i in range(10):
            c += 1
            print('{} x {:2} = {}'.format(n, c, (n * c)))
print('FIM.')
