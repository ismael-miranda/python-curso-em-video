'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
estatistica = []
jogadores = {}
quant_gols = []
total = 0
resp = ''
while True:
    total = 0
    print('»'*35)
    jogadores['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for p in range(1, partidas+1):
        gols = int(input(f'Quantos gols na partida {p}? '))
        total += gols
        quant_gols.append(gols)
    jogadores['gols'] = quant_gols[:]
    jogadores['total'] = total
    estatistica.append(jogadores.copy())
    quant_gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break

print(f'»'*35)
print(f'{"cod":<4}{"nome":<12}{"gols":<12}{"total":>4}')
print('-'*35)
for p, v in enumerate(estatistica):
    print(f'{p:<4}{v["nome"]:<12}{str(v["gols"]):<12}{v["total"]:>4}')

while True:
    print('─'*35)
    jogador = int(input('Mostrar dados de qual jogador? (Ecerrar 999) '))
    if jogador == 999:
        print('««« VOLTE SEMPRE »»»')
        break
    elif jogador >= len(estatistica):
        print('Código inexistente')
    else:
        print(f'Levantamento do jogador {estatistica[jogador]["nome"]}')
        for pos, g in enumerate(estatistica[jogador]['gols']):
            print(f'  → Na partida {pos}, foram {g} gols')
