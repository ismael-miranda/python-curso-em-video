'''
Faça um programa que leia o sexo de uma pessoa, mas so aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
ate ter um valor correto.
'''

sexo = True
while sexo:
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        print('O sexo digitado foi {}'.format(sexo))
        sexo = False
    else:
        print('Sexo digitado foi {}'.format(sexo))
        print('Digite M ou F')
        print('-'*20)