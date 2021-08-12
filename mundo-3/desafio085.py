'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
dados = [[], []]
cont_par = cont_impar = 0
for d in range(1, 8):
    num = int(input(f'Digite o {d}º valor:'))
    if num % 2 == 0:
        if cont_par == 0 or num > dados[0][-1]:
            dados[0].append(num)
        else:
            pos_par = 0
            while pos_par < len(dados[0]):
                if num <= dados[0][pos_par]:
                    dados[0].insert(pos_par, num)
                    break
                pos_par += 1
        cont_par += 1
    else:
        if cont_impar == 0 or num > dados[1][-1]:
            dados[1].append(num)
        else:
            pos_impar = 0
            while pos_impar < len(dados[1]):
                if num <= dados[1][pos_impar]:
                    dados[1].insert(pos_impar, num)
                    break
                pos_impar += 1
        cont_impar += 1
print(dados[0])
print(dados[1])
