import desafio108_moeda

valor = float(input('Digite o preço R$ '))
print(f'A metade de {desafio108_moeda.moeda(valor)} é '
      f'{desafio108_moeda.moeda(desafio108_moeda.metade(valor))}')
print(f'O dobro de {desafio108_moeda.moeda(valor)} é '
      f'{desafio108_moeda.moeda(desafio108_moeda.dobro(valor))}')
print(f'{desafio108_moeda.moeda(valor)} com 15% de desconto '
      f'{desafio108_moeda.moeda(desafio108_moeda.diminuir(valor, 15))}')
print(f'{desafio108_moeda.moeda(valor)} com 33% de aumento '
      f'{desafio108_moeda.moeda(desafio108_moeda.aumentar(valor, 33))}')
