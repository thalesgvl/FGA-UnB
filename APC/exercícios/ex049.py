n = int(input('\033[32mDigite um número para ver sua tabuada: \033[m'))
for i in range(1, 11):
    print('\033[33m{}\033[m \033[34mx\033[m \033[33m{:2}\033[m \033[34m=\033[m \033[33m{}.\033[m'.format(n, i, (n * i)))