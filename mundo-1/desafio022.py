nome = input('Digite seu nome completo: ')
print('Nome com as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com as letras minúsculas: {}'.format(nome.lower()))

# outra forma de tirar os espaços
#print('Total de letras sem espaços: {}'.format(len(nome)-nome.count(' '))
nome_sem_espaco = nome.replace(' ', '')
print('Total de letras sem espaços: {}'.format(len(nome_sem_espaco)))

primeiro_nome = nome.split()

print('Tota de letras do primeiro nome: {}'.format(len(primeiro_nome[0])))