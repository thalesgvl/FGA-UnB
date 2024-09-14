s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        s += i
        c += 1
print('\n\033[34mA soma de todos os: {} valores solicitados é de: {}.\033[m'.format(c, s))
