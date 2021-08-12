def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return f'{res:.2f}'


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return f'{res:.2f}'


def dobro(preco):
    res = preco * 2
    return f'{res:.2f}'


def metade(preco):
    res = preco / 2
    return f'{res:.2f}'
