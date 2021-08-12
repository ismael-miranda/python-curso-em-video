total = acima_mil = menor_preco = cont = 0
nome_produto = ''
continuar = ''
print('×'*22)
print('Lojas Bolso Furado')
print('×'*22)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total = total + preco
    if preco > 1000:
        acima_mil += 1

    if cont == 1:
        menor_preco = preco
        nome_produto = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_produto = produto

    while True:
        continuar = str(input('Quer continuar? S / N → ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('{:×^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {acima_mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_produto} que custa R$ {menor_preco:.2f}')
