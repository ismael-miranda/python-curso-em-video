n = int(input('Digite quantos termos de Fibonacci vc quer mostar: '))
t1 = 0
t2 = 1
t3 = 0
cont = 0
print('{} -> {}'.format(t1,t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
