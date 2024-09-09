nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome em minúsculas é: {}.'.format(nome.lower()))
print('Seu nome possui ao todo: {} letras.'.format(nome.__len__() - nome.count(' ')))
print('Seu primeiro nome é: {} e ele possui: {} letras.'.format(separa[0], len(separa[0])))
print('Seu último nome é: {} e ele possui: {} letras.'.format(separa[-1], len(separa[-1])))

