from datetime import date
atual = date.today().year
ano_nasc = int(input('Qual o ano de nascimento?: '))
idade = (atual - ano_nasc)
print('O atleta possui:\033[34m {} anos.\033[m'.format(idade))

if idade <= 9:
    print('Classificação: \033[34mMIRIM.\033[m')
elif idade <= 14:
    print('Classificação: \033[34mINFANTIL.\033[m')
elif idade <= 19:
    print('Classificação: \033[34mJUNIOR.\033[m')
elif idade <= 25:
    print('Classificação: \033[34mSÊNIOR.\033[m')
else:
    print('Classificação: \033[34mMASTER.\033[m')