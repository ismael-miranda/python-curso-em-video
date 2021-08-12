'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
'''
print('-'*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-'*40)
lista = ('Escova de dentes', 9.75, 'Sabonete', 1.50, 'Creme dental', 4.23,
         'Shampoo', 18.99, 'Fio dental', 3.40, 'Protetor Solar', 35.80,
         'Condicionador de Cabelo', 20.10, 'Aparelho de babear', 21.50,
         'Desodorante', 9.50, 'Gel para Cabelo', 7.19)
for produtos in lista:
    if type(produtos) == str:
        print('{:.<30}'.format(produtos), end='')
    if type(produtos) == float:
        print('R$ {:>6.2f}'.format(produtos))
print('-'*40)
