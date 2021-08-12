ano = int(input('Digite o ano para saber se ele é bissexto: '))

if ano % 4 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))