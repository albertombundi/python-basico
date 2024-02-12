# teste = list()
# teste.append('Alberto')
# teste.append(20)
# malta = list()
# malta.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = '22'
# malta.append(teste[:])
# print(malta)

# pessoal = [['Jão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in pessoal:
#  print(f'{p[0]} tem {p[1]} anos de idade.')

pessoal = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoal.append(dados[:])
    dados.clear()
for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
