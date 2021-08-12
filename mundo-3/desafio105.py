def notas(*num, sit=False):
    """
    >>Função para analisar notas e situação de varios alunos.
    :param num: uma ou varias notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não aparecer a situação
    :return: dicionário com várias informações sobre a turma.
    """
    boletim = {'total': len(num)}
    maior = menor = soma = 0
    for p, n in enumerate(num):
        soma += n
        if p == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['media'] = soma / len(num)
    if sit:
        if boletim['media'] < 5:
            boletim['situacao'] = 'RUIM'
        elif boletim['media'] < 7:
            boletim['situacao'] = 'RAZOÁVEL'
        else:
            boletim['situacao'] = 'BOA'
    return boletim, num


valor = notas(10, 5, 8, 3)
print(valor)
help(notas)
