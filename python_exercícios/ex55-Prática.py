maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O mair peso lido foi de  {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))





