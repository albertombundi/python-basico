def aumentar(preço=0, taxa=0, formato=False):
    """
    Função para calcular a moeda
    :param preço: indica o valor do preço
    :param taxa: o valor da taxa
    :param formato: mostra se o formato do preço é True ou False.
    :return: ainda não entendi bem essa função.
    Função criada por Alberto Soneha Mbundi.
    """
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
