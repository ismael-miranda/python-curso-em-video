r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if r1<r2+r3 and r2<r1+r3 and r3<r2+r1:
    print('Com essas retas podemos criar um triangulo')
