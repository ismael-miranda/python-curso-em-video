produto = float(input('Informe o valor do produto R$ '))

print('*'*50)
print('\033[1;32mCondições de pagamento:\033[m')
print('1 - à vista dinheiro/cheque, com 10% de desconto')
print('2 - à vista no cartão, com 5% de desconto')
print('3 - Em até 2X no cartão, sem desconto')
print('4 - Acima de 3X, com 20% de juros')
print('*'*50)

condicao = int(input('\033[1;33mEscolha uma opção: \033[m'))

if condicao <= 0 or condicao > 4:
    print('Essa não é uma opção valida!')
elif condicao == 1:
    produto_desc = produto - (produto * 10 / 100)
    print('Valor do produto com desconto R$ {:.2f}'.format(produto_desc))
elif condicao == 2:
    produto_desc = produto - (produto * 5 / 100)
    print('Valor do produto com desconto R$ {:.2f}'.format(produto_desc))
elif condicao == 3:
    valor_parcela = produto / 2
    print('Valor da parcela R$ {:.2f}'.format(valor_parcela))
elif condicao == 4:
    quant = int(input('Quantidade de parcelas: '))
    produto = produto + (produto * 20 / 100)
    valor_parcela = produto / quant
    print('Valor do produto com 20% R$ {} e valor da parcela R$ {:.2f}'.format(produto, valor_parcela))
