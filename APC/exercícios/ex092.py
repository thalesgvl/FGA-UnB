from datetime import datetime

pessoa = dict()



pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['ano_nasc'] = int(input('Digite seu ano de nascimento: '))
pessoa['carteira_trab'] = int(input('Digite o n° da carteira de trabalho [0 caso não tenha]: '))

pessoa['idade'] = datetime.now().year - pessoa['ano_nasc']


if pessoa['carteira_trab'] != 0:
    pessoa['ano_contrato'] = int(input('Digite o ano da contratação: '))
    pessoa['salario'] = int(input('Digite o salário: '))
    pessoa['idade_aposentadoria'] = (pessoa['ano_contrato'] + 35) - datetime.now().year + pessoa['idade']

print('-=' * 30)

for k, v in pessoa.items():
    print(f' - {k} é igual a: {v}.')
