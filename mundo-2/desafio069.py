maior_idade = 0
#homem cadastrado = h_cadastrado
h_cadastrados = 0
#mulher menor de 21  = m_menor
m_menor = 0
cont = 0
while True:
    print('-'*25)
    print('Cadastre uma pessoa')
    print('-'*25)
    idade = int(input('Qual a sua idade? '))
    while True:
        sexo = str(input('Qual o sexo [M / F]: ')).upper().strip()[0]
        if sexo in 'MF':
            break
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        h_cadastrados += 1
    if sexo == 'F':
        if idade < 20:
            m_menor += 1
    cont += 1
    print('-'*25)
    while True:
        continuar = str(input('Quer continuar |S / N|? ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('==== Fim do Programa ====')
print(f'Foram cadastradas {cont} pessoas.')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao total temos {h_cadastrados} homens cadastrados.')
print(f'Temos {m_menor} mulheres com menos de 20 anos.')
