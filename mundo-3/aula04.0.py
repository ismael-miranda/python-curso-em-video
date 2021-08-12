def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def dobra(lista):
    print(lista)
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos] * 2
        pos = pos + 1
    print(lista)

#Programa Principal
soma(4, 7)
soma(9, 2)
soma(10, 11)

lst = [2, 9, 4, 5, 1, 4]
lst1 = [1, 2, 3, 7, 6]
dobra(lst)
dobra(lst1)