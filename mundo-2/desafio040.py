nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('Aluno aprovado, nota {}'.format(media))
elif 5.0 >= media < 7.0:
    print('Aluno em recuperação, nota {}'.format(media))
else:
    print('Aluno reprovado')
