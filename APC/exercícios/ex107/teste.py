import moeda

p = float(input('Digite o preço: R$'))

print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'Aumentando 15%, temos: R${moeda.aumentar(p, 15)}')
print(f'Diminuindo 35%, temos: R${moeda.diminuir(p, 35)}')
