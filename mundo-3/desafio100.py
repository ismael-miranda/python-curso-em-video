"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
"""
from random import randint
from time import sleep


def sorteia(num):
    print('Sorteando 5 valores da lista:', end=' ')
    for n in range(0, 5):
        num.append(randint(1, 10))
        print(num[n], end=' ', flush=True)
        sleep(0.5)

    print('PRONTO!')


def somaPar(par):
    soma = 0
    for p in par:
        if p % 2 == 0:
            soma = soma + p
    print(f'Somando os valores pares sorteados {par}, temos {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
