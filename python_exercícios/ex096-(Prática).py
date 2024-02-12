def área(larg, camp):
    a = larg * camp
    print(f'A área de um terreno {larg}x{camp} é de {a}m².')


# Programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
