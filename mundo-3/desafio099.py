"""
Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
"""

from time import sleep
from random import randint


def linha():
    print('¬'*50)


def maior(*valor):
    num_maior = 0
    print('Analisando os valores informados...')
    # print(max(valor))
    for v in valor:
        print(f'{v} ', end='', flush=True)
        sleep(0.75)
        if num_maior < v:
            num_maior = v
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {num_maior}.')
    linha()


linha()
maior(1, 3, 7, 2, 4, 10)
maior(randint(1, 3), randint(4, 7), randint(8, 10))
maior(randint(1, 5), randint(6, 10))
maior(randint(1, 10))
maior()
