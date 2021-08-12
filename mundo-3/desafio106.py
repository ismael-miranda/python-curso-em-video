'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa se encerrará. Importante: use cores.
'''


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('¬'*tam)
    print('  {}'.format(msg))
    print('¬'*tam)

#Programa principal
comando = ''
while True:
    titulo('Sistema de ajuda PyHELP')
    comando = str(input('Função ou Biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Até logo!')
