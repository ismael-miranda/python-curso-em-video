aluguel = float(input('Quantos dias o carro foi alugado? '))
km = float(input('KM percorrido: '))

total = (aluguel * 60) + (km * 0.15)

print('Total a pagar R${}'.format(total))