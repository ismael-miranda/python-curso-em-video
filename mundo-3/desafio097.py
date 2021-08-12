'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''


def msg(texto):
    tam = len(texto) + 4
    print('¬'*tam)
    print(f'  {texto}')
    print('¬'*tam)


msg('Ismael Miranda')
msg('Estou aprendendo PYTHON')
msg('Dia')
