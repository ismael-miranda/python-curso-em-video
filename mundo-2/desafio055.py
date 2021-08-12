pesado = 0
leve = 0
for cont in range(0+1,6):
    peso = float(input('Digite o peso {}: (Kg) '.format(cont)))
    if peso > pesado:
        pesado = peso
    elif peso < pesado:
        leve = peso

print('O maior peso é Kg {:.2f}'.format(pesado))
print('O menor peso é Kg {:.2f}'.format(leve))
