'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
nome_peso = list()
armazena = []
maior = menor = 0
while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(int(input('Peso: ')))
    if len(armazena) == 0:
        maior = menor = nome_peso[1]
    else:
        if nome_peso[1] > maior:
            maior = nome_peso[1]
        if nome_peso[1] < menor:
            menor = nome_peso[1]
    armazena.append(nome_peso[:])
    nome_peso.clear()
    resp = ''
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('¬'*27)
print(f'Foram cadastradas {len(armazena)}')
print(f'O maior peso foi de {maior} Kg. Peso de',end=' ')
for a in armazena:
    if a[1] == maior:
        print(f'[{a[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor} Kg. Peso de', end=' ')
for a in armazena:
    if a[1] == menor:
        print(f'[{a[0]}]', end=' ')
print(armazena)
