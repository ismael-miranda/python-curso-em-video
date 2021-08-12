'''Faça um programa que mostre na tela uma contagem regressiva
para estouro de fogos de artifício. Indo de 10 até 0, com
uma pausa  de 1 segundo entre eles.'''
from time import sleep

for conta in range(10, -1, -1):
    print(conta)
    sleep(1)
print('BOOM')