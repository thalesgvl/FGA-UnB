def area(l, c):
    a = l * c
    print(f'A área de um terreno com {l:.2f}x{c:.2f} é igual a: {a:.2f}m².')

#PROGRAMA PRINCIPAL
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
