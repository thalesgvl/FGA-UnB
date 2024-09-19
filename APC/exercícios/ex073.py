times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo',
         'Bragantino', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
         'Internacional', 'Palmeiras', 'Santos', 'São Paulo','Vasco')
print('=' * 30)
print(f'Os cinco primeiros colocados são: {times[0:6]}.')
print('=' * 30)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 30)
print(f'O time do Goiás está na posição: {times.index("Goiás")+1}.')
print('=' * 30)