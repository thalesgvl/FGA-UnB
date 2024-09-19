lnum = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
lnum_e = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número (0 a 20): '))
    if 0 <= n <= 20:
        for i in lnum:
            if n == i:
                print('Você digitou o número: {}.'.format(i))
                print('Por extenso é: {}.'.format(lnum_e[i].capitalize()))
        break
    else:
        print('Tente novamente. ', end= '')
