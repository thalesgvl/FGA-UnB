jogador = dict()

gols = []

jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} participou: '))

for i in range(jogador['partidas']):
    saldo_gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {i}: '))
    gols.append(saldo_gols)

jogador['gols'] = list(gols)
jogador['total'] = sum(list(gols))

print('-=' * 30)

for k, v in jogador.items():
    print(f'{k} é igual a: {v}.')

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, marcou: {v} gols.')
