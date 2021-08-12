'''
Faça um programa que leia um número qualquer e mostre o seu fatorail
'''

numero = int(input('Digite um número inteiro: '))
fatorial = 1
print('O fatorial {}! é '.format(numero), end='')
while numero > 0:
    if numero > 1:
        print(numero, end='x')
    else:
        print(numero,end=' = ')
    fatorial = fatorial * numero
    numero -= 1

print(fatorial)