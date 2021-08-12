soma_par = 0
for conta in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma_par += num
print('A soma dos pares digitados é {}'.format(soma_par))