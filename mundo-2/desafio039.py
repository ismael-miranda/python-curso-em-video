from datetime import datetime

ano_nascimento = str(input('Digite seu ano de nascimento: '))
ano_nasc = datetime.strptime(ano_nascimento, '%Y')
atual = datetime.today()
resultado = abs(((atual - ano_nasc) / 365).days)

prazo_alistar = resultado - 18

if resultado == 18:
    print('É hora de se alistar')
elif resultado > 18 and resultado < 45:
    print('Você passou {} para se alistar'.format(prazo_alistar))
else:
    print('Ainda faltam {} anos para se alistar'.format(-prazo_alistar))
