def leiaInt(msg):
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            break
        else:
            print('\033[0;1;31mERRO! Digite um número inteiro válido.\033[m')
    return valor


numero = leiaInt('Digite um número: ')
print('Você digitou o número {}.'.format(numero))
