from random import choice
from time import sleep

opcao = int(input('''\033[36mPedra-Papel-Tesoura!:\033[m
\033[33m[1]\033[m Pedra.
\033[33m[2]\033[m Papel.
\033[33m[3]\033[m Tesoura.
\033[36mQual a sua jogada?:\033[m '''))

if opcao == 1:
    opcao = 'Pedra'
elif opcao == 2:
    opcao = 'Papel'
elif opcao == 3:
    opcao = 'Tesoura'

cpu = choice(['Pedra', 'Papel', 'Tesoura'])


print('\033[35mJO\033[m')
sleep(0.4)
print('\033[35mKEN\033[m')
sleep(0.5)
print('\033[35mPO ! ! !\033[m')
sleep(0.6)

#empate
if opcao == cpu:
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[33mEMPATE!\033[m'''.format(opcao, cpu))
#todas derrotas possiveis
if opcao == 'Pedra' and cpu == 'Papel':
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[31mVitória do computador.\033[m'''.format(opcao, cpu))
if opcao == 'Papel' and cpu == 'Tesoura':
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[31mVitória do computador.\033[m'''.format(opcao, cpu))
if opcao == 'Tesoura' and cpu == 'Pedra':
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[31mVitória do computador.\033[m'''.format(opcao, cpu))
#todas vitorias possiveis
if opcao == 'Pedra' and cpu == 'Tesoura':
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[32mVitória do jogador!\033[m'''.format(opcao, cpu))
if opcao == 'Papel' and cpu == 'Pedra':
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[32mVitória do jogador!\033[m'''.format(opcao, cpu))
if opcao == 'Tesoura' and cpu == 'Papel':
    print('''Jogador jogou: \033[34m{}.\033[m
Computador jogou: \033[34m{}.\033[m
\033[32mVitória do jogador!\033[m'''.format(opcao, cpu))
