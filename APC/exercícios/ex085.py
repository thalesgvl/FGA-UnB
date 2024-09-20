num = [[], []]

for i in range(7):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]}.')
print(f'Os valores ímpares digitados foram: {num[1]}.')
