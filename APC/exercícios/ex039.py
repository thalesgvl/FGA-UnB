from datetime import date
atual = date.today().year

ano_nasc = int(input('Ano de nascimento: '))

idade = (atual - ano_nasc)

print('Quem nasceu em: {}, possui {} anos em {}.'.format(ano_nasc, idade, atual))

if idade == 18:
    print('Seu alistamendo ocorrerá este ano. Aliste-se imediatamente.')
elif idade > 18:
    print('Seu alistamento já passou há: {} anos.'.format(idade - 18))
    print('Ano do alistamento: {}.'.format(ano_nasc + 18))
elif idade < 18:
    print('Seu alistamento ocorrerá daqui a: {} anos.'.format(18 - idade))
    print('Ano do alistamento: {}.'.format(ano_nasc + 18))


