preco = float(input('Digite o valor do produto: '))

desconto = preco * 0.05

preco = preco - desconto

print('Produto com 5% de desconto, novo valor R${:.2f}'.format(preco))