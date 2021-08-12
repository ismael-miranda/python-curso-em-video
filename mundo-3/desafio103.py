def ficha(jogador='', gol=0):
    if jogador == '':
        return 'O jogador <desconhecido> fez {} gol(s) no campeonato.'.format(gol)
    else:
        return 'O jogador {} fez {} gol(s) no campeonato.'.\
            format(jogador, gol)


nome_jogador = str(input('Nome do Jogador: '))
while True:
    gols = str(input('Número de Gols: '))
    if gols.isnumeric():
        gols = int(gols)
        break
    elif gols == '':
        gols = 0
        break
    else:
        print('Digite um valor inteiro para os número de Gols')

print(ficha(nome_jogador, gols))