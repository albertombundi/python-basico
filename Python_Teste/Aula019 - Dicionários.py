# pessoas = {'Nome': 'Alberto', 'Sexo': 'M', 'Idade': 20}
# pessoas['peso'] = '98.5'
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
# for k, v in pessoas.items():
#    print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[1]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
