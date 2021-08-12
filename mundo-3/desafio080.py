'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''
valor = []
numero = 0
maior = 0
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if numero > maior:
        maior = numero
        valor.append(maior)
        print('Adicionado no final da lista')
    else:
        for val in range(0, 5):
            if numero <= valor[val]:
                valor.insert(val, numero)
                print(f'O número foi adicionado na posção {val}')
                break

print(valor)
print('«»'*30)
lista = []
num = 0

for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos}.')
                break
            pos += 1

print(lista)