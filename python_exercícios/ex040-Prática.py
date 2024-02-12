nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(nota1, nota2, média))
# if média >=5 and média < 7:
if 7 > média >=5:
    print('O aluno está em \033[1:1:34mRECUPERAÇÃO.')
elif média < 5:
    print('O aluno está \033[1:1:31mREPROVADO.')
elif média >= 7 :
    print('O aluno esá \033[1:1:32mAPTO.')


