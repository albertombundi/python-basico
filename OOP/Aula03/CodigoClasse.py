class Meu_Objeto:
    def __init__(pessoa, nome, idade):
        pessoa.nome = nome
        pessoa.idade = idade
        print('Chamando o contrutor')

    def imprime(pessoa):
        print('Olá o meu nome é %s e eu tenho %d anos'%(pessoa.nome, pessoa.idade))


Pedro = Meu_Objeto("Alberto", 21)
Pedro.imprime()