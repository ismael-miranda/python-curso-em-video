'''
Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input('Média: '))
if boletim['media'] < 5:
    boletim['situacao'] = 'Reprovado'
elif boletim['media'] < 7:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Aprovado'
print('¬'*35)
for aluno, dados in boletim.items():
    print(f'  - {aluno} é igual {dados}')
