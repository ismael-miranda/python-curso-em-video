'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
'''
#Solução 1 - by Ismael
from random import randint
aleatorio = 0
num = ()
for cont in range(0, 5):
    aleatorio = randint(1, 10)
    num = num + (aleatorio,)
print(f'O valores sorteados foram {num}')
print(f'O maior valor sorteado foi {sorted(num)[-1]}')
print(f'O menor valor sorteado foi {sorted(num)[0]}')

#Solução 2 - Professor
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),
           randint(1,10))
print(f'Os valores sorteados são: ',end='')
for n in numeros:
    print(f'{n} ',end='')
print(f'\nO maior valor {max(numeros)}')
print(f'O menor valor {min(numeros)}')