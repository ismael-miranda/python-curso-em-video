'''

Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar - [2]multiplicar - [3]maior - [4]novos numeros - [5]sair do programa

'''

sair = ''
soma = 0
multiplica = 0
while sair != '5':
    valor1 = int(input('Digite o 1º valor: '))
    valor2 = int(input('Digite o 2º valor: '))
    print('='*5, 'Escolha uma opção no menu abaixo: ', '='*5)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Numeros\n[5] Sair')
    print('='*47)
    escolha = str(input('Opção escolhida: '))
    if escolha == '1':
        soma = valor1 + valor2
        print('A soma dos dois valores são {}'.format(soma))
    elif escolha == '2':
        multiplica = valor1 * valor2
        print('A multiplicação dos dois valores são {}'.format(multiplica))
    elif escolha == '3':
        if valor1 > valor2:
            print('O 1º valor é o maior')
        else:
            print('O 2º valor é o maior')
    elif escolha == '4':
        sair = '0'
    else:
        sair = '5'
        print('Sistema Finalizado')
