# Para criar uma DOCSTRING usa-se 3 pares de aspas duplas """"""
# Server para descrever a funcionalidade da função/metodo

def contador(i, f, p):
    """
    ->Faz uma contagem e mostra o resultado na tela
    :param i:inicio da contagem
    :param f:fim da contagem
    :param p:passo da contagem,
    :return:sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(5, 11, 2)
