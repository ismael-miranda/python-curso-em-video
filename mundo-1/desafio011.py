altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

area = altura * largura #metros quadrados
tinta = area / 2

print('Area {:.2f}\nQuantidade de tinta {:.2f} litros'.format(area,tinta))