resp = 'S'
soma = quant = méd = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Queres continuar? [S/N] ')).upper().strip()[0]
méd = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, méd))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
