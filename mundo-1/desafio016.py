from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {}, e sua parte inteira é {}'.format(num, trunc(num)))
#pode ser usado o casting explicito para fazer esse exercicio:
#usa-se int(num) - neste caso