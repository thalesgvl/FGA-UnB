dados_pessoas = dict()

dados = []
soma = media_idade = 0

while True:
    dados_pessoas['nome'] = str(input('Digite o nome: '))
    while True:
        dados_pessoas["sexo"] = str(input('Digite o sexo [M/F]: ')).upper().strip()
        if dados_pessoas["sexo"] in 'MmFf':
            break
        else:
            print('Opção inválida. Tente novamente.')

    dados_pessoas['idade'] = int(input('Digite a idade: '))
    soma += dados_pessoas['idade']

    while True:
        r = str(input('Deseja realizar outro cadastro[S/N]?: '))

        if r in 'Ss' or r in 'Nn':
            break
    
        else:
            print('Opção inválida. Tente novamente.')
        
    dados.append(dados_pessoas.copy())

    if r in 'Nn':
        break
        
media_idade = soma/len(dados)

print('-=' * 30)
print(f'Quantidade de pessoas cadastradas: {len(dados)}.')
print()
print(f'A média de idade foi de: {media_idade:5.2f}.')
print()
print(f'As mulheres cadastradas foram:')

for i in dados:
    if i['sexo'] in 'Ff':
        print(f' {i["nome"]}')
print()

print(f'Lista de pessoas acima da média de idade: ')

for i in dados:
    if i['idade'] > media_idade:
        print('')
        for k, v in i.items():
            print(f'{k} = {v} ', end='')
        print()
    