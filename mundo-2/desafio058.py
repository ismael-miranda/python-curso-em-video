'''
Melhore o jogo do desafio 28. Onde o computador vai "pensar" um numero entre 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''
from random import randint
print('Tente adivinhar qual numero o computador está pensando')
num_pc = 0
cont = 0
palpite = -1
#print(palpite, num_pc)
while num_pc != palpite:
    palpite = int(input('Qual numero de 0 à 10 estou pensando?'))
    num_pc = randint(0,10)
    cont += 1
    print(num_pc, palpite)
    if num_pc == palpite:
        print('Parabéns, você acertou:')
        print('O computador pensou {} e você {}'.format(num_pc, palpite))
        print('Você precisou de {} palpites para acertar'.format(cont))
    else:
        print('Você não acertou, tente novamente')