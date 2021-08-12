r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if r1<r2+r3 and r2<r1+r3 and r3<r2+r1:
    print('Com essas retas podemos criar um triangulo')
    if r1 == r2 == r3:
        print('Todos os lados são iguais, forma um triangulo Equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Dois lados são iguais, forma uma triangulo Isósceles.')
    elif r1 != r2 != r3 != r1:
        print('Todos os lados são diferentes, forma um triangulo Escaleno.')
else:
    print('Essas retas não formam triangulo.')