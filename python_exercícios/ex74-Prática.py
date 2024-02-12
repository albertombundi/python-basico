from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Os valores sorteados são: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado é: {max(números)}')
print(f'O menor valor sorteado é: {min(números)}')
