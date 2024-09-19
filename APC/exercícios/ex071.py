print('=' * 50)
print('BANCO GVL'.center(50))
print('=' * 50)
valor = int(input('Qual o valor do saque?: '))
total = valor
ced = 100
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        print('Total de: {} cédulas de: R${}.'.format(tot_ced, ced))
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        tot_ced = 0
        if total == 0:
            break

