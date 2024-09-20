from random import randint
from time import sleep

sena = []
jogos = []
c = 0

n_jogos = int(input('Digite a quantidade de jogos desejada: '))
              
for i in range(n_jogos):

    while len(sena) != 6:
        num = randint(1, 60)
        if num not in sena:
            sena.append(num)
        else:
            num = randint(1, 60)

    jogos.append(sena[:])
    sena.clear()

print(f'-=-=-= SORTEANDO {n_jogos} JOGOS: -=-=-=')

for i in range (n_jogos):
    sleep(0.5)
    print(f'Jogo {i+1:^2}: {jogos[0+c]}')
    c += 1
