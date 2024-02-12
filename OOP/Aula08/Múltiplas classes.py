class Animal:
    def __init__(anim, cor, genero, andar):
        anim.cor = cor
        anim.genero = genero
        anim.num_de_patas = andar

    def falar(anim):
        print('Olá, sou um cachorro e sei falar.')

    def andar(anim):
        print('Estou andar sobre %i patas' % anim.num_de_patas)

    def amamentar(anim):
        if anim.genero.lower()[0] == 'm':
            print("Macho não amamentam")
            return
        print("Amamentando meu filhote")


# Rex = Animal('marron', 'masculino', 4)
# Rex.falar()
# Rex.andar()
# Rex.amamenta()


class Pessoa(Animal):
    def __init__(anim, cor, genero, andar, cabelo):
        super(Pessoa, anim).__init__(cor, genero, andar)
        anim.cabelo = 'Castanho'

    def falar(anim):
        super(Pessoa, anim).falar()
        print('Olá, sou uma pessoa e sei falar.')


Hugo = Pessoa('branco', 'masculino', 2, 'castanho')
Hugo.falar()
