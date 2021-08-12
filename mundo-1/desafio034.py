salario = float(input('Informe seu salário:R$ '))

if salario > 1250:
    salario = salario * 1.10
if salario < 1250:
    salario = salario * 1.15
print('Seu no salário é R${}'.format(salario))