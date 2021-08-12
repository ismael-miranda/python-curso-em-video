'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
num = cont = 0
lista = []
resp = ''
while True:
    num = int(input('Digite um valor: '))
    if cont == 0 or num < lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num >= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
    cont +=1
print(f'Você digitou {len(lista)} elementos.')
print(f'O valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')

# #Solucao Professor
# valores = []
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print(f'Você digitou {len(valores)} elementos.')
# valores.sort(reverse=True)
# print(valores)
# if 5 in valores:
#     print('O valor 5 faz parte da lista!')
# else:
#     print('O valor 5 não faz parte da lista!')