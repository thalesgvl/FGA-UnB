def ficha(nome= '<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou: {gols} gol(s) no campeonato.')



#PROGRAMA PRINCIPAL
n = str(input('Nome do jogador: '))
g = str(input('Gols marcados: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
