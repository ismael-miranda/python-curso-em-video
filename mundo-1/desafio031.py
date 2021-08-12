viagem = float(input('Qual a distancia da viagem em KM? '))

if viagem > 200:
    viagem = viagem * 0.45
    print('Sua viagem custará R${:.2f}'.format(viagem))
else:
    viagem = viagem * 0.50
    print('Sua viagem custará R${:.2f}'.format(viagem))