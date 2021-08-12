#Exemplo1
# lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
# print(lanche)
# print(lanche[1])
# print(lanche[3])
# print(lanche[-2])
# print(lanche[1:3])
# print(lanche[-2:])
# print(lanche[-3:])

#Exemplo2
# lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
# for comida in lanche:
#     print(f'Eu comerei {comida}')
# print('Estou satisfeito!')

#Exemplo3
# lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(len(lanche))
# for cont in range(0, len(lanche)):
#     print(f'Eu comerei {lanche[cont]} na posição {cont}')

#Exemplo4
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu comerei {comida} na posição {pos}')

print(sorted(lanche))