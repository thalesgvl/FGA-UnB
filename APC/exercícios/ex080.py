list_num = []

for i in range(5):

    num = int(input('Digite um valor para lista: '))
    if i == 0 or num > list_num[-1]:
        list_num.append(num)
        print(f'Valor adicionado ao final da lista.')

    else:
        pos = 0
        while pos < len(list_num):
            if num <= list_num[pos]:
                list_num.insert(pos, num)
                print(f'Valor adicionado na posição: {pos}')
                break
            pos += 1

print(list_num)
