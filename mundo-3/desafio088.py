'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
# q = quantidade de sorteio
# j = jogos
# s = sorteios
'''
from random import randint
from time import sleep

print('─'*35)
print('{:^35}'.format('Jogo da Mega Sena'))
print('─'*35)
quant_sorteio = int(input('Quantos jogos você quer sortear? '))
jogos = []
verifica = 0
for q in range(0, quant_sorteio):
    jogos.append([])
    cont = 0
    for j in range(0, 6):
        numeros = randint(1, 60)
        if verifica == numeros:
            while verifica == numeros:
                numeros = randint(1, 60)
        verifica = numeros
        if cont == 0 or numeros > jogos[q][-1]:
            jogos[q].append(numeros)
        else:
            pos = 0
            while pos < len(jogos[q]):
                if numeros <= jogos[q][pos]:
                    jogos[q].insert(pos, numeros)
                    break
                pos += 1
        cont += 1

print(f'─'*8, 'Sorteando', quant_sorteio, 'Jogos', '─'*8)
num = 1
for s in jogos:
    print(f'Jogo {num}: {s}')
    sleep(1)
    num += 1
print('{:─^35}'.format(' BOA SORTE! '))
