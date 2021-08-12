'''
Crie uma tupla preenchida com os 20 colocados da tabela do brasileirão,
na ordem de colocação. Depois mostre:
a-Os 5 primeiros
b-Os 4 últimos colocados
c-Times em ordem alfabética.
d-Em que posição está o time da Chapecoense.
'''

brasileirao = ('Flamengo', 'Palmeiras', 'Santos', 'Internacional', 'Corinthians',
               'São Paulo', 'Bahia', 'Grêmio', 'Atlético-MG', 'Botafogo',
               'Athletico-PR', 'Vasco', 'Ceará', 'Fortaleza', 'Goiás', 'Fluminense',
               'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('{:×^50}'.format(' Lista de times do Brasileirão 2019 '))
print(brasileirao)
print('×'*50)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('×'*50)
print(f'Os 4 ultimos são {brasileirao[-4:]}')
print('×'*50)
print(f'Times em ordem alfabética {sorted(brasileirao)}')
print('×'*50)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')
for pos, cont in enumerate(brasileirao):
    if cont == 'Chapecoense':
        print(f'O Chapecoense está na {pos+1}ª posição')
