num = int(input('Informe um número: '))
# = str(num)
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(n[3]))
print('unidade: {}'.format(u))
# print('Dezena: {}'.format(n[2]))
print('dezena: {}'.format(d))
# print('Centena: {}'.format(n[1]))
print('centena: {}'.format(c))
# print('Milhar: {}'.format(n[0]))
print('Milhar: {}'.format(m))

