sexo = str(input('Informe seu sexo[M/F]: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida. Por favor, digite seu sexo[M/F]: '))
print('Sexo {} registrado com sucesso.'.format(sexo))