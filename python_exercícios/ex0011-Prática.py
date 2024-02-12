larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
tin = área / 2
print('para pintar essa parede você vai precisar de {}l de tinta.'.format(tin))

