#Listas
num = [2,5,9,1]
print(num)
#alterando um valor da lista
num[2] = 3
print(num)
#adicionar um valor no final da lista
num.append(7)
print(num)
#adicionar um valor em local especifico da lista
#num.insert(posicao, valor)
num.insert(2, 0)
print(num)
#odenar a lista em ordem crescente
num.sort()
print(num)
#ordenar a lista em ordem decrescente
num.sort(reverse=True)
print(num)
#quanidade de elementos na lista
print(f'Essa lista tem {len(num)} elementos.')
#deletar um elemento usando pop
#por default o pop exclui o último elemento
num.pop()
print(num)
#determinando qual elemento será deletado com pop
num.pop(4)
print(num)