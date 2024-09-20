list_num = []

while True:

    num = int(input('Digite um valor para a lista: '))
    list_num.append(num)
    r = str(input('Deseja continuar[S/N]?: ')).strip()
    if r in 'Nn':
        break

print(f'Foram digitados: {len(list_num)} números.')

c = sorted(list_num)
d = sorted(list_num, reverse=True)
print(f'Lista em ordem crescente: {c}.')
print(f'Lista em ordem decrescente: {d}.')

if 5 in list_num:
    print('O número 5 foi encontrado na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
