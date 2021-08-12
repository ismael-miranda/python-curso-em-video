termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
total = 0
continua = 10
while continua != 0:
    total = total + continua
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    continua = int(input('Quantos termos vc quer mostrar a mais? '))
print('Progressão finalizada, foram mostrados {} termos'.format(total))