distância = float(input('Qual é a distância da sua viagem? '))
print('Voce está prestes a começar uma viagem de {}km.'.format(distância))
# if distância <= 200:
#  preço = distância * 0.50
# else:
#  preço = distância * 0.45
preço= distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
