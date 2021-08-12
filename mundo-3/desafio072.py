'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá  ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um valor entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente. ',end='')
    else:
        print('Você digitou o número "{}"'.format(numeros[num]))
        continua = str(input('Quer continuar? [S/N]')).upper()
        if continua == 'N':
            break
