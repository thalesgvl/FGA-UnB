c_idade = c_sexom = c_sexofi = 0
while True:
    print('-' * 50)
    print('Cadastramento.'.center(50))
    print('-' * 50)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    r = str(input('Deseja realizar outro cadastro? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
    elif r == 'S':
        if idade > 18:
            c_idade += 1
        if sexo == 'M':
            c_sexom += 1
        if sexo == 'F' and idade < 20:
            c_sexofi += 1
    else:
        print('Resposta inválida. Tente novamente.')
print('Total de pessoas com mais de 18 anos: {}.'.format(c_idade))
print('Ao todo temos: {} homens cadastrados.'.format(c_sexom))
print('E temos: {} mulher(es) com menos de 20 anos.'.format(c_sexofi))
