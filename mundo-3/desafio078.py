'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
na lista.
'''
# valores = []
# posicao = 0
# for v in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# print('¬'*50)
# print(f'Você digitou os valores {valores}')
# print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
# for pos, val in enumerate(valores):
#     if max(valores) == val:
#         print(f'{pos} ', end='')
# print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
# for pos, val in enumerate(valores):
#     if min(valores) == val:
#         print(f'{pos} ', end='')

#solucao professor
listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')
for p, val in enumerate(listanum):
    if val == menor:
        print(f'{p}...',end='')
print()
