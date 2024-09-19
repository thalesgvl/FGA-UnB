from random import randint
cpu = randint(0, 20)
c = 0
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Par ou ímpar [P/I]?: ')).strip()[0]
    s = (cpu + n)
    if r in 'Pp':
        if s % 2 ==  0:
            print('''Você escolheu par! Sua jogada foi: {} e o computador jogou: {}.
A soma foi: {}. Você ganhou!'''.format(n, cpu, s))
            c += 1
        else:
            print('''Você escolheu par! Sua jogada foi: {} e o computador jogou: {}.
A soma foi: {}. Você perdeu.'''.format(n, cpu, s))
            break
    elif r in 'Ii':
        if s % 2 != 0:
            print('''Você escolheu ímpar! Sua jogada foi: {} e o computador jogou: {}.
A soma foi: {}. Você ganhou!'''.format(n, cpu, s))
            c += 1
        else:
            print('''Você escolheu ímpar! Sua jogada foi: {} e o computador jogou: {}.
A soma foi: {}. Você perdeu.'''.format(n, cpu, s))
            break
    else:
        print('Resposta inválida. Tente novamente.')
print('Game Over! Você venceu {} vezes.'.format(c))
