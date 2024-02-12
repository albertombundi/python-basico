salário = float(input('Qual é o salário do fucncinário?$'))
novo = salário + (salário * 15/100)
print('um funcionário que ganhava ${:.2f}, com 15% de aumento, passa a receber ${:.2f}'.format(salário, novo))
