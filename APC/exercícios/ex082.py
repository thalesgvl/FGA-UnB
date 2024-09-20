list_num = []
list_num_par = []
list_num_impar = []

while True:
    num = int(input('Digite um valor: '))
    list_num.append(num)

    r =  str(input('Deseja adicionar outro valor[S/N]?: ')).strip()
    if r in 'Nn':
        break

for n in list_num:
    if n % 2 == 0: 
        list_num_par.append(n)
    else:
        list_num_impar.append(n)

print(f'Lista de números: {list_num}.')
print(f'Lista de números (par): {list_num_par}.')
print(f'Lista de números (ímpar): {list_num_impar}.')
