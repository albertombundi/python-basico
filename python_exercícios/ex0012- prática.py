preço = float(input('Qual é o preço do produto? $'))
novo = preço - (preço * 5 / 100)
print(' o prduto que custava ${:.2f}, na promoção de desconto de 5% vai custar ${:.2f}'.format(preço, novo))


