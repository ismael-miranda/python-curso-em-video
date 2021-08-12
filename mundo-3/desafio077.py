'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = ('cachorro', 'pato', 'galinha', 'computador')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    vogal = ''
    for pa in p:
        for v in vogais:
            if v in pa:
                vogal += ' ' + v
    print('Na palavra {} temos{}'.format(p.upper(), vogal))

#Solução Professor
for pa in palavras:
    print('\nNa palavra {} temos '.format(pa.upper()),end='')
    for letra in pa:
        if letra in 'aeiou':
            print(letra, end=' ')