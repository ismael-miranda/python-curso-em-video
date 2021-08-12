from datetime import datetime

ano_nascimento = str(input('Qual ano de nascimento - dia/mes/ano: '))
ano_nasc = datetime.strptime(ano_nascimento, '%d/%m/%Y')
atual = datetime.today()
resultado = abs(((atual - ano_nasc) / 365).days)

if resultado > 25:
    print('Sua categoria é MASTER')
elif 25 == resultado > 19 :
    print('Sua categoria é SENIOR')
elif 19 == resultado > 14:
    print('Sua categoria é JUNIOR')
elif 14 == resultado > 9:
    print('Sua categoria é INFANTIL')
else:
    print('Sua categoria é MIRIM')
