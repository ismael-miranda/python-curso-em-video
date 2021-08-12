'''
Crie um programa  que leia uma frase qualquer e diga
se ela é um palindromo, desconciderando os espaços
'''
frase = str(input('Digite: ')).strip().upper()
frase = frase.replace(' ', '')

if frase[::-1] == frase:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo')

#Outra forma de resolver o mesmo desafio
#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split() -> tirar os espaços da frase e cria uma lista
#junto = ''.join(palavras) -> junta as palavras sem espaços
#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#   inverso += junto[letra]
#print(junto, inverso)