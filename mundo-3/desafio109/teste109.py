import desafio109_moeda

valor = float(input('Digite o preço R$ '))
print(f'A metade de {desafio109_moeda.moeda(valor)} é '
      f'{desafio109_moeda.metade(valor, True)}')
print(f'O dobro de {desafio109_moeda.moeda(valor)} é '
      f'{desafio109_moeda.dobro(valor, True)}')
print(f'{desafio109_moeda.moeda(valor)} com 15% de desconto '
      f'{desafio109_moeda.diminuir(valor, 15, True)}')
print(f'{desafio109_moeda.moeda(valor)} com 33% de aumento '
      f'{desafio109_moeda.aumentar(valor, 33, True)}')
