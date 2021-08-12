'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
cadastro = []
pessoa = {}
resp = ''
media = tot_idade = cont_f = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('¬'*35)
print(f'- O Grupo tem {len(cadastro)} pessoas.')
for m in cadastro:
    tot_idade = tot_idade + m['idade']
media = tot_idade / len(cadastro)
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for feminino in cadastro:
    if feminino['sexo'] in 'Ff':
        print(feminino['nome'], end=' ')
print(f'\n- Lista das pessoas que estão acima da média:')

for acima in cadastro:
    if acima['idade'] > media:
        print(f'\nnome = {acima["nome"]}; sexo = {acima["sexo"]}; idade = {acima["idade"]}')
print('<<< ENCERADO >>>')
