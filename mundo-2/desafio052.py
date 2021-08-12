num = int(input('Digite um numero: '))
total = 0
for cont in range(1, num+1):
    if num % cont == 0:
        total += 1
        print('\033[1;32m', end='')
    else:
        print('\033[1;33m',end='')

    print('{} '.format(cont), end='')

print('\n\033[m0 numero {} foi dividido {} vezes'.format(num, total))
if total == 2:
    print('Numero primo')
else:
    print('Não é primo')