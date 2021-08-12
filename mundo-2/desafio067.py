while True:
    num = int(input('Que ver a tabuada do? '))
    if num < 0:
        print('Programa tabuada ENCERRADO.')
        break
    print('»'*25)
    for tabuada in range(1,11):
        resultado = num * tabuada
        print(f'{num} X {tabuada} = {resultado}')
    print('«'*25)