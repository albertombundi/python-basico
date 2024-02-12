# print('\033[7;33;44mOlá, Mundo!\033[m')
# a = 3
# b = 5
# print('os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Alberto'
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'preto e branco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['preto e branco'], nome, cores['limpa']))

