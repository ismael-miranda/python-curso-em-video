'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com
a formatação correta.
'''
lista = [[], [], []]
linha = coluna = 0
while coluna < 3:
    while linha < 3:
        num = int(input(f'Digite um valor para [{coluna}, {linha}]: '))
        linha += 1
        lista[coluna].append(num)
    linha = 0
    coluna += 1
print('→'*32)
for c in lista:
    for l in c:
        print('[{:^4}]'.format(l), end='')
    print('')
