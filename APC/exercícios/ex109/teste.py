import moeda

p = float(input('Digite o preço: R$'))

print(f'O dobro de {moeda.moeda(p)} é: {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é: {moeda.metade(p, True)}')
print(f'Aumentando 15%, temos: {moeda.aumentar(p, 15, True)}')
print(f'Diminuindo 35%, temos: {moeda.diminuir(p, 35, True)}')