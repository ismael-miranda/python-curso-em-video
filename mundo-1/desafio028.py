from random import randint
print('Tente advinhar qual número o computador está pensando!')
pc = int(input('Qual numero de 0 à 5 estou pensando? '))
num_pc = randint(0,5)
if pc == num_pc:
    print('Parabéns')
else:
    print('O computador venceu!')
    print('Número digitado {} \nNúmero pensado {}'.format(pc, num_pc))
