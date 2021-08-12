'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
estatistica = {}
quant_gols = []
total = 0
estatistica['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {estatistica["nome"]} jogou? '))
for p in range(1, partidas+1):
    gols = int(input(f'Quantos gols na partida {p}? '))
    total = total + gols
    quant_gols.append(gols)
estatistica['gols'] = quant_gols[:]
estatistica['total'] = total
print('¬'*40)
print(estatistica)
print('¬'*40)
for k, v in estatistica.items():
    print(f'O campo {k} tem o valor {v}.')
print('¬'*40)
print(f'O jogador {estatistica["nome"]} jogou {partidas} partidas.')
for p, j in enumerate(estatistica['gols']):
    print(f'   → Na partida {p+1}, fez {j} gols.')
print(f'Foi um total de {estatistica["total"]} gols')
