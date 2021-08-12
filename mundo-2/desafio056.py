media_idade = 0
velho = 0
homem = ''
mulher = ''
nova = 0
idade_menor = 0
for pessoas in range(0+1, 5):
    print('------ {}ª ------'.format(pessoas))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo (M)/(F): ')).strip().upper()
    if idade > velho and sexo == 'M':
        velho = idade
        homem = nome
    if idade < 20 and sexo == 'F':
        nova = idade
        mulher = nome
        idade_menor += 1
    media_idade = (media_idade + idade)

print('A média de idade do grupo é {:.2f}'.format(media_idade/pessoas))
print('O nome do home mais velho é {} e sua idade é {} anos'.format(homem,velho))
print('Mulhers com menos de 20 anos são {}'.format(idade_menor) )
print('O nome da mulher mais nova é {} e sua idade é {} anos'.format(mulher,nova))
