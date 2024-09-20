matriz = [[],[],[]]

sum_par = sum_3_col = 0

for linha in range(0,3):
        for coluna in range(0,3):
                matriz[linha].append(int(input(f"Digite um valor para [{linha},{coluna}]: ")))

print('-='*30)
for linha in range(0,3):
        for coluna in range(0,3):
                print(f'[{matriz[linha][coluna]:^5}]', end='')

                if matriz[linha][coluna] % 2 == 0:
                        sum_par += matriz[linha][coluna]
                
        print()

print(f'A soma dos valores pares é: {sum_par}.')

for linha in range(3):
       sum_3_col += matriz[linha][2]

print(f'A soma dos valores da terceira colula é: {sum_3_col}.')

print(f'O maior número da linha (2) é: {max(matriz[1])}.')