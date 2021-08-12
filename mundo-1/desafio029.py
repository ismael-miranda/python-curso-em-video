velocidade = float(input('Qual velocidade do carro? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Velocidade permitida 80KM/h, você passou a {}KM/h'.format(velocidade))
    print('Multa por KM excedente R${:.2f}'.format(multa))
