'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
geradas.
'''
resp = ''
cont = 0
lista_p = [] #lista principal
lista_par = []
lista_impar = []
lista_c = [] #lista numeros cresecentes
lista_d = [] #lista numeros decrescentes
while True:
    num = int(input('Digite um valor: '))
    if num == 0:
        break
    lista_p.append(num)
    if cont == 0 or num > lista_c[-1]:
        lista_c.append(num)
    else:
        pos = 0 #posicao
        while pos < len(lista_c):
            if num <= lista_c[pos]:
                lista_c.insert(pos, num)
                break
            pos += 1
    if cont == 0 or num < lista_d[-1]:
        lista_d.append(num)
    else:
        posicao = 0
        while posicao < len(lista_d):
            if num >= lista_d[posicao]:
                lista_d.insert(posicao, num)
                break
            posicao += 1
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
    cont += 1
for par in lista_p:
    if par % 2 == 0:
        lista_par.append(par)
    else:
        lista_impar.append(par)

print(f'A lista completa é {lista_p}')
print(f'A lista em ordem crescente é {lista_c}')
print(f'A lista completa em ordem decrescente é {lista_d}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')
