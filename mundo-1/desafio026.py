frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A útilma letra A apareceu na posição {}'.format(frase.rfind('A')+1))