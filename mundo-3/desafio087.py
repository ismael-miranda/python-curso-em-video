'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
lista = [[], [], []]
# terceira coluna → maior valor da segunda linha
linha = coluna = pares = t_coluna = maior = 0
while coluna < 3:
    while linha < 3:
        num = int(input(f'Digite um valor para [{coluna}, {linha}]: '))
        linha += 1
        lista[coluna].append(num)
    linha = 0
    coluna += 1
print('-'*32)
for pos, c in enumerate(lista):
    if pos == 1:
        for m in c:
            if maior < m:
                maior = m
    t_coluna = t_coluna + c[-1]
    for l in c:
        if l % 2 == 0:
            pares = pares + l
        print('[{:^3}]'.format(l), end='')
    print('\n', end='')
print('-'*32)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {t_coluna}')
print(f'O maior valor da segunda linha é {maior}')
