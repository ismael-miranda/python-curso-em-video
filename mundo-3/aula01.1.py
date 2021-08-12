a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
a = a + b
print(type(a))
print(b)
print(c)
print(d)
#Contar quantas vezes há um elemento
print(c.count(5))
#Mostrar em qual posição(index) está um elemento
print(c.index(8))