'''
Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas ja sao maiores.
'''

from datetime import date

maior_idade = 0
menor_idade = 0
for nascimento in range(1, 8):
    data_nasc = int(input('Digite a data de nascimento {}: '.format(nascimento)))
    atual = date.today().year
    idade = atual - data_nasc
    if idade >= 21:
        maior_idade = maior_idade + 1
    else:
        menor_idade += 1
print('Pessoas com 21 anos ou mais {}'.format(maior_idade))
print('Pessoas menores de idade {}'.format(menor_idade))