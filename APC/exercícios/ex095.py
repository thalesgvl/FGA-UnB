jogador = dict()

gols = []
dados_jogadores = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} participou: '))

    gols.clear()
    
    for i in range(jogador['partidas']):
        saldo_gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {i}: '))
        gols.append(saldo_gols)

    jogador['gols'] = list(gols)
    jogador['total'] = sum(list(gols))

    dados_jogadores.append(jogador.copy())


    r = str(input('Deseja cadastrar outro jogador?[S/N]: '))

    if r in 'Nn':
        break

print('-=' * 30)

for k, v in enumerate(dados_jogadores):
    print(f'{k:>4} ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end= '')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador[999 para parar]?: '))
    if busca == 999:
        break
    if busca >= len(dados_jogadores):
        print('Erro. Não existe jogador com este código.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {dados_jogadores[busca]["nome"]}: ')
        for i, v in enumerate(dados_jogadores[busca]["gols"]):
            print(f'Na partida: {i+1}. Foi marcado: {v} gols.')