'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


def area(largura, comprimento):
    total = largura * comprimento
    print(f'A área  de um terreno de {largura}X{comprimento} é de {total}m².')


print('Área do Terreno')
print('¬'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
