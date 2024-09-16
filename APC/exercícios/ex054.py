from datetime import date
atual = date.today().year
cmaior = 0
cmenor = 0
for i in range(1,8):
    ano_nasc = int(input('Em qual ano a {}ª pessoa nasceu: '.format(i)))
    idade = atual - ano_nasc
    if idade >= 21:
        cmaior += 1
    else:
        cmenor += 1
print('Ao todo possuem: {} pessoas maiores de idade, e {} pessoas menores de idade.'.format(cmaior, cmenor))
