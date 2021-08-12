'''
Faça um progama  que calcule a soma entre todos os
numeros impares  que são multiplos  de tres e que se
encontram no intervalo de 1 a 500.
'''
soma = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        print(impar)
        soma += impar
print(soma)