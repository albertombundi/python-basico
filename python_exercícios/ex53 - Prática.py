frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
# inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palídromo!')



