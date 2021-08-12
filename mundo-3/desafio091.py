'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
jogo['jogador1'] = randint(1, 6)
jogo['jogador2'] = randint(1, 6)
jogo['jogador3'] = randint(1, 6)
jogo['jogador4'] = randint(1, 6)
print('→→ Valores Sorteados')
for k, v in jogo.items():
    sleep(0.7)
    print(f'   O {k} tirou {v}')
pos = 6
cont = 1
print('¬'*30)
print('=== RANKING DOS JOGADORES ===')
while pos > 0:
    for k, v in jogo.items():
        if pos == v:
            print(f'   {cont}º lugar: {k} com {v}')
            cont +=1
    pos -= 1

####SOLUCAO PROFESSOR

jogando = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogando.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.7)
ranking = sorted(jogando.items(), key=itemgetter(1), reverse=True)
print('¬'*35)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(0.7)
