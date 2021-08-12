num1 = float(input('Primiro valor: '))
num2 = float(input('Segundo valor: '))
num3 = float(input('Terceiro valor: '))

menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
print('Menor {:.0f}'.format(menor))

maior = num1
if num2>num3 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('Maior {:.0f}'.format(maior))