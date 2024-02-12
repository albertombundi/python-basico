peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[1:1:31mABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS! você está na faixa do \033[1:1:32mPESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em \033[1:1:33mSOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em \033[1:1:34mOBESIDADE!')
elif imc >= 40:
    print('Você está em \033[1:1:35mOBESIDADE MÓRBIDA\033[0:0:m. cuidado!')



