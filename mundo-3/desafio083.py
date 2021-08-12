'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
'''
lista= []
cont = 0
conta = 0
lista.append(str(input('Digite uma expressão: ')))
for v in lista:
    for va in v:
        if '(' in va:
            cont += 1
        elif ')' in va:
            conta += 1
if cont == conta:
    print('Expressão válida.')
else:
    print('Sua expressão está errada!')
