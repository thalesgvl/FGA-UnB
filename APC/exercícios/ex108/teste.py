import moeda

p = float(input('Digite o preço: R$'))

print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 15%, temos: {moeda.moeda(moeda.aumentar(p, 15))}')
print(f'Diminuindo 35%, temos: {moeda.moeda(moeda.diminuir(p, 35))}')