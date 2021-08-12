def fatorial(numero, show=False):
    """
    ->Calcula o fatorial de um número
    :param numero: O valor a ser calculado
    :param show: (Opcional) mostrar ou não a conta
    :return: retorna o valor de número
    """
    fat = 1
    print('¬'*28)
    while numero > 0:
        if show:
            if numero == 1:
                print('{}'.format(numero), end=' = ')
            else:
                print('{}'.format(numero), end=' * ')
        fat = fat * numero
        numero -= 1
    return fat


print(fatorial(5, True))
help(fatorial)
