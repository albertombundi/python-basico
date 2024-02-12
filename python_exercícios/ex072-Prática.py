perg = ' '
cont = ('zero', 'um', 'dois', 'Três', 'Quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezasseis', 'dezassete', 'desoito',
        'dezanove', 'vinte')
while True:
    núm = int(input('Digite um  número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')
