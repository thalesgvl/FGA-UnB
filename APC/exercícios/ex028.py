from random import choice
from time import sleep

n = int(input('Digite um número entre 0 e 5: '))
list_n = [0, 1, 2, 3, 4, 5]
cpu_n = choice(list_n)

print('Processando...')
sleep(2)

if n == cpu_n:
    print('Parabéns, você ganhou! O número: {} foi o sorteado!'.format(cpu_n))
else:
    print('Você perdeu, o número sorteado foi: {}.'.format(cpu_n))
