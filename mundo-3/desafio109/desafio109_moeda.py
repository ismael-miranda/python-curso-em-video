def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    if formato == False:
        return res
    else:
        return moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    if formato is False:
        return res
    else:
        return moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    if formato is False:
        return res
    else:
        return moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
