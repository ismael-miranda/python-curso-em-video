parar = 0
cont = 0
soma = 0
while parar != 999:
    numero = int(input('Digite um numero *999 para parar*: '))
    if numero == 999:
        parar = numero
    else:
        soma = soma + numero
        cont +=1
print('Foram digitados {} numeros e a soma entre eles é {}'.format(cont,soma))