'''numero = input('Digite um número: ')

print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))'''

numero_b = int(input('Digite um número: '))

milhar = numero_b // 1000 % 10
centena = numero_b // 100 % 10
dezena = numero_b // 10 % 10
unidade = numero_b // 1 % 10

print('unidade:{}'.format(unidade))
print('dezena:{}'.format(dezena))
print('centena:{}'.format(centena))
print('milhar:{}'.format(milhar))

