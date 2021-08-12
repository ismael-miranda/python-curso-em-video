'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = date.today().year - int(input('Ano Nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['ctps'] == 0:
    print('¬'*35)
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
else:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = date.today().year - cadastro['contratacao'] + 35
    print('¬' * 35)
for k, v in cadastro.items():
    print(f'{k.capitalize()} tem o valor \033[1;34m{v}\033[m')
