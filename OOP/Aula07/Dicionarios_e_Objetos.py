Pessoa = {'Nome': 'Alberto', 'Profissao': 'Programador', 'Idade': 20}

Pessoa['Nome'] = 'Roberto'
print(Pessoa['Nome'])


class Pessoa:
    pass


Hugo = Pessoa()

Hugo.nome = 'Alberto'
Hugo.emprego = 'Programador'
Hugo.Idade = 21

print(Hugo.__dict__)
