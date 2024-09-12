p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
media = (p1 + p2) / 2

if media <= 5:
    print('\033[31mReprovado.\033[m')
elif media > 5 and media <= 6.9:
    print('\033[33mRecuperação.\033[m')
elif media >= 7:
    print('\033[32mAprovado.\033[m')