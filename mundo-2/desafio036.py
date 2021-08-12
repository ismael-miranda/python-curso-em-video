'''
Escreva um programa para aprovar o emprestimo bancario
para compra de uma casa. O programa vai perguntar o valor
da casa, o salario do comprador e em quantos anos ele vai pagar.
-Calcule o valor da prestação mensal
-A prestacao nao pode passar de 30% do salario
'''

valor_casa = float(input('Informe o valor da casa R$ '))
salario = float(input('Digite seu salario R$ '))
anos = int(input('Em quantos anos prestações deseja pagar? '))

#sal_30 = 30% do salario
sal_30 = salario * 30 / 100
#val_pres = valor da prestacao
val_pres = valor_casa / (anos * 12)

if sal_30 < val_pres:
    print('Nessas condições não podemos liberar o empréstimo')
    print('30% do seu salário R$ {:.2f}'.format(sal_30))
    print('Valor da prestação R$ {:.2f}'.format(val_pres))
else:
    print('\033[33mEmpréstimo liberado. Parabéns pela compra.')
    print('Valor da prestação R$ {:.2f}'.format(val_pres))

#print(sal_30)
#print(val_pres)
