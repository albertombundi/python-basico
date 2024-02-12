núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[m O numéro {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('e por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
