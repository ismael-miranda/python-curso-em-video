import math

angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
