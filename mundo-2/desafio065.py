cont = num = soma = maior = menor = 0
n = validador = True
continua = ''
while n:
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
    if num > maior:
        maior = num
    elif num < maior:
        menor = num
    while validador:
        continua = str(input('Quer continuar [S/N]: ')).strip().upper()
        if continua == 'S' or continua == 'N':
            validador = False
        else:
            print('Valor digitado inválido!')
    validador = True
    if continua == 'N':
        n = False

media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
