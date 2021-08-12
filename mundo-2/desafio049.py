num = int(input('Digite um numero para fazer a tabuada: '))

for tabuada in range(1, 11):
    print('{} X {} = {}'.format(num, tabuada, num * tabuada))
