s_idade = 0
velho = 0
novo = 0
nome_velho = ''
mulher_menor20 = 0
for pess in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    s_idade += idade
    m_idade = (s_idade / 4)

    if sexo in 'Mm' and pess == 1:
        velho = idade
        nome_velho = nome
    if sexo in 'Mm' and velho < idade:
            velho = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menor20 += 1
        
print('A média de idade do grupo é de: {}.'.format(m_idade))
print('O homem mais velho se chama: {}. E possui: {} anos.'.format(nome_velho, velho))
print('Ao todo são: {} mulheres com menos de 20 anos.'.format(mulher_menor20))
