from random import randint

soma = 0
cont = 0
print('¬'*25)
print('Vamos Jogar Par ou Ímpar')
print('¬'*25)
while True:
    num = randint(1, 10)
    valor = int(input('Digite um valor: '))
    soma = valor + num
    while True:
        escolha = str(input('Par ou Impar: [P/I]')).upper().strip()
        if escolha in 'PI':
            break
    if escolha == 'P':
        if soma % 2 == 0:
            print('─'*30)
            print(f'Você jogou {valor} e computador {num}. Total de {soma} DEU PAR.')
            print('─'*30)
            cont += 1
            print('Você Venceu!')
            print('Vamos jogar novamente...')
            print('¬'*30)
        else:
            print('─'*30)
            print(f'Você jogou {valor} e o computador {num}. Total de {soma} DEU IMPAR.')
            print('─'*30)
            print('Você perdeu!')
            print('¬'*30)
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('─'*30)
            print(f'Você jogou {valor} e o computador {num}. Total de {soma} DEU PAR.')
            print('─'*30)
            print('Você perdeu!')
            print('¬'*30)
            break
        else:
            print('─'*30)
            print(f'Você jogou {valor} e o computador {num}. Total de {soma} DEU IMPAR.')
            print('─'*30)
            cont += 1
            print('Você venceu!')
            print('Vamos jogar novamente...')
            print('¬'*30)
print(f'GAME OVER! Você venceu {cont} vezes.')
