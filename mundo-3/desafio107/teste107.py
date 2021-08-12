import desafio107_moeda

valor = float(input('Digite o preço R$ '))
print(f'A metade de R$ {valor} é R$ {desafio107_moeda.metade(valor)}')
print(f'O dobro de R$ {valor} é R$ {desafio107_moeda.dobro(valor)}')
print(f'R$ {valor} com 15% de desconto R$ {desafio107_moeda.diminuir(valor, 15)}')
print(f'R$ {valor} com 33% de aumento R$ {desafio107_moeda.aumentar(valor, 33)}')
