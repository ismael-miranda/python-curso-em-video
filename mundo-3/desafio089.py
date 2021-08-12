'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
a = alunos
n = notas
'''
from time import sleep
alunos = []
media = 0
#inicio cadastro de nome e notas
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = ''
    while True:
        resp = str(input('Quer continuar: [S/N]')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
#Fim cadastro nome e notas
#Inicio mostra nomes e medias
print('¬'*35)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*28)
for posicao, aluno in enumerate(alunos):
    print(f'{posicao:<4}{aluno[0]:<10}{aluno[-1]:>8.1f}')
while True:
    print('-'*30)
    mostra_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostra_aluno == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    else:
        print(f'Notas de {alunos[mostra_aluno][0]} são {alunos[mostra_aluno][1]}')
print('«««« VOLTE SEMPRE »»»»')
