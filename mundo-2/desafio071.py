nota50 = nota20 = nota10 = nota1 = 0
while True:
    saque = int(input('Que valor você quer sacar? R$ '))
    nota50 = saque // 50
    resto50 = saque % 50
    nota20 = resto50 // 20
    resto20 = resto50 % 20
    nota10 = resto20 // 10
    nota1 = resto20 % 10

    if nota50 > 0:
        print(f'Total de {nota50} notas de R$ 50,00')
    if nota20 > 0:
        print(f'Total de {nota20} ntoas de R$ 20,00')
    if nota10 > 0:
        print(f'Total de {nota10} notas de R$ 10,00')
    if nota1 > 0:
        print(f'Total de {nota1} nota de R$ 1,00')
    break
