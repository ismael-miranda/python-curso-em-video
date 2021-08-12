'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.
'''
valores = []
numero = 0
resp = ''
while True:
    numero = int(input('Digite um valor: '))
    if numero in valores:
        print('Valor duplicado! Não vou adicionar')
    else:
        valores.append(numero)
        print('Valor adicionado com sucesso!')
    resp = str(input('Quer continuar? [S/N]: ')).upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper()
    if resp == 'N':
        break
valores.sort()
print('»'*40)
print(valores)