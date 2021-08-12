"""
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep


def linha():
    print('¬'*35)


def contador(inicio, fim, passo):
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}', end='')
    if inicio < fim:
        print()
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.7)
        print('FIM!')
    elif inicio > fim:
        print()
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ', flush=True)
            sleep(0.7)
        print('FIM!')


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
comeco = int(input('Inicio: '))
final = int(input('Final:  '))
intervalo = int(input('Passo:  '))
contador(comeco, final, intervalo)
