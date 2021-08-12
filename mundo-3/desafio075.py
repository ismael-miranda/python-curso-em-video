'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
n = 0
valores = ()
frase = ('um', 'outro', 'mais um', 'o último')
num9 = 0
num3 = 0
par = ()
for c in frase:
    inteiros = int(input(f'Digite {c} número: '))
    valores = valores + (inteiros,)
print('»'*40)
print(f'Você digitou os valores {valores}')
print('»'*40)
for pos, valida in enumerate(valores):
    if valida == 9:
        num9 += 1
    if valida == 3:
        num3 = pos + 1

print(f'O valor 9 apareceu {num9} vezes.')
if num3 != 0:
    print(f'O valor 3 apareceu na {num3}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram', end=' ')
for pares in valores:
    if pares % 2 == 0:
        print(pares, end=' ')

#solução professor
numeros = (int(input('\nDigite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))
print(f'Os valores digitos foram {numeros} ')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')