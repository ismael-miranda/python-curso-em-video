valores = []
valores.append(4)
valores.append(8)
valores.append(1)
print(valores)
for v in valores:
    print(v,' ', end='')
print()
for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}.')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for pos, val in enumerate(valores):
    print(f'O valor {val} está na posição {pos}.')
print(valores)
valores.sort()
print(valores)