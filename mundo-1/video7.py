n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
soma = n1+n2
subtracao = n1 - n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponencial = n1 ** n2

print('A soma é {}, a subtracao {} e a divisao {:.3f}'.format(soma, subtracao, divisao))
print('Divisao inteira {} e potência {}'.format(divisao_inteira, exponencial))