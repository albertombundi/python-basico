times = ('Corithians', 'Palmeiras', 'Santos', 'Grêmios',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí' 'Ponte Preta',
         'Atlético-GO')
print('--' * 15)
print(f'Lista de Times do Brasileirão: {times}')
# for t in times:
# print(t)
print('--' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')

