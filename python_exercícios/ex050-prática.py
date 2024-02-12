soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Você informou {} número/s \033[1:1:32mPARES\033[0:0:0m e a soma foi {}'.format(cont, soma))




