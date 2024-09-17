from random import randint
cpu = randint(0, 10)
c = 0
jogador = ''
print('Tente adivinhar qual número pensei de 0 a 10.')
while cpu != jogador:
    jogador = int(input('Qual o seu palpite?: '))
    if cpu > jogador:
        print('Mais... Tente mais uma vez.')
        c += 1
    else:
        print('Menos... Tente mais uma vez.')
        c += 1
print('Acertou com {} tentativas. Parabéns!'.format(c))